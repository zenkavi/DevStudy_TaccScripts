import glob
import nibabel as nib
from nistats.first_level_model import FirstLevelModel
import numpy as np
import os
import pandas as pd
import re
from argparse import ArgumentParser

#Usage: python level_1.py -s SUBNUM
#Outputs:
#WHAT DOES RANDOMISE NEED FOR LATER MULTIPLE COMPARISON CORRECTIONS?

parser = ArgumentParser()
parser.add_argument("-s", "--subnum", help="subject number")
subnum = args.subnum
data_loc = os.environ['DATA_LOC']

events_files = glob.glob('%s/sub-*/func/sub-*_task-machinegame_run-*_events.tsv'%(data_loc))
events_files.sort()

out_path = "%s/derivatives/nistats/level_1/sub-%s"%(data_loc,subnum)
if not os.path.exists(out_path):
    os.mkdir(out_path)

all_events = pd.DataFrame()

for cur_ef in events_files:
    df = pd.read_csv(cur_ef, sep = '\t')
    all_events = all_events.append(df, ignore_index= True)

all_events = all_events[all_events['response_time'].notnull()]
all_events.response_time = all_events.response_time/1000
mean_rt = all_events.response_time.mean()

del all_events

sub_events = [x for x in events_files if subnum in x]

def make_contrasts(design_matrix):
        # first generate canonical contrasts (i.e. regressors vs. baseline)
    contrast_matrix = np.eye(design_matrix.shape[1])
    contrasts = dict([(column, contrast_matrix[i])
                      for i, column in enumerate(design_matrix.columns)])

    # Add more complex contrasts
    contrasts['task_on'] = (contrasts['m1'] + contrasts['m2'] + contrasts['m3'] + contrasts['m4'])
    contrasts['rt'] = (contrasts['m1_rt'] + contrasts['m2_rt'] + contrasts['m3_rt'] + contrasts['m4_rt'])
    contrasts['gain-loss'] = contrasts['gain'] - contrasts['loss']
    contrasts['loss-gain'] = contrasts['loss'] - contrasts['gain']

    return contrasts

def add_transform(dataframe, columns=None, type=None):
    if columns is None:
        columns = dataframe.columns
    if type == "td":
        td = dataframe.loc[:,columns].apply(np.gradient)
        td.iloc[0,:] = 0
        for i,col in td.iteritems():
            insert_loc = dataframe.columns.get_loc(i)
            dataframe.insert(insert_loc+1, i+'_td', col)
    if type == "sq":
        sq = dataframe.loc[:,columns].apply(np.square)
        sq.iloc[0,:] = 0
        for i,col in sq.iteritems():
            insert_loc = dataframe.columns.get_loc(i)
            dataframe.insert(insert_loc+1, i+'_sq', col)

for run_events in sub_events:

    runnum = re.findall('\d+', os.path.basename(run_events))[1]

    #fmri_img: path to preproc_bold that the model will be fit on
    fmri_img = os.path.join(data_loc,"derivatives/fmriprep_1.3.0/fmriprep/sub-%s/func/sub-%s_task-machinegame_run-%s_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz"%(subnum, subnum, runnum))

    #read in preproc_bold for that run
    cur_img = nib.load(fmri_img)
    #CHANGE THIS TO CORRECT HEADER ATTRIBUTE
    cur_img_tr = cur_img.header['pixdim'][4]

    #read in events.tsv for that run

    #process events for GLM
    #events: 4 col events file for WHOLE RUN with onset, duration, trial_type, modulation
    #trial_type column:
        #m1, m2, m3, m4 - onset: stimulus_presentation onset, duration: mean_rt, modulation: 1
        #m1_rt, m2_rt, m3_rt, m4_rt - onset: stimulus_presentation, duration: mean_rt, modulation: rt-mean_rt
        #gain - onset: response onset, duration: response duration, modulation: gain-mean_gain
        #loss - onset: reponse onset, duration: response duration, modulation: loss-mean_loss
        #junk: onset: response onset, duration: response duration, modulation: 1
    #confounds:
        #6 movement + squares
        #scrubbing ?

    cur_events = pd.read_csv(run_events, sep = '\t')

    cond_m1 = cur_events.query('trial_type == "stim_presentation" & stimulus == 1')[['onset']]
    cond_m1['duration'] = mean_rt
    cond_m1['modulation'] = 1
    cond_m1['trial_type'] = 'm1'
    cond_m2 = cur_events.query('trial_type == "stim_presentation" & stimulus == 2')[['onset']]
    cond_m2['duration'] = mean_rt
    cond_m2['modulation'] = 1
    cond_m2['trial_type'] = 'm2'
    cond_m3 = cur_events.query('trial_type == "stim_presentation" & stimulus == 3')[['onset']]
    cond_m3['duration'] = mean_rt
    cond_m3['modulation'] = 1
    cond_m3['trial_type'] = 'm3'
    cond_m4 = cur_events.query('trial_type == "stim_presentation" & stimulus == 4')[['onset']]
    cond_m4['duration'] = mean_rt
    cond_m4['modulation'] = 1
    cond_m4['trial_type'] = 'm4'

    cur_events['rt_shift'] = cur_events.response_time.shift(-1)

    cond_m1_rt = cur_events.query('trial_type == "stim_presentation" & stimulus == 1')[['onset', 'rt_shift']]
    cond_m1_rt['duration'] = mean_rt
    cond_m1_rt['modulation'] = cond_m1_rt['rt_shift'] - mean_rt
    cond_m1_rt = cond_m1_rt.drop(['rt_shift'], axis=1)
    cond_m1_rt['trial_type'] = "m1_rt"
    cond_m2_rt = cur_events.query('trial_type == "stim_presentation" & stimulus == 2')[['onset', 'rt_shift']]
    cond_m2_rt['duration'] = mean_rt
    cond_m2_rt['modulation'] = cond_m2_rt['rt_shift'] - mean_rt
    cond_m2_rt = cond_m2_rt.drop(['rt_shift'], axis=1)
    cond_m2_rt['trial_type'] = "m2_rt"
    cond_m3_rt = cur_events.query('trial_type == "stim_presentation" & stimulus == 3')[['onset', 'rt_shift']]
    cond_m3_rt['duration'] = mean_rt
    cond_m3_rt['modulation'] = cond_m3_rt['rt_shift'] - mean_rt
    cond_m3_rt = cond_m3_rt.drop(['rt_shift'], axis=1)
    cond_m3_rt['trial_type'] = "m3_rt"
    cond_m4_rt = cur_events.query('trial_type == "stim_presentation" & stimulus == 4')[['onset', 'rt_shift']]
    cond_m4_rt['duration'] = mean_rt
    cond_m4_rt['modulation'] = cond_m4_rt['rt_shift'] - mean_rt
    cond_m4_rt = cond_m4_rt.drop(['rt_shift'], axis=1)
    cond_m4_rt['trial_type'] = "m4_rt"

    cond_gain = cur_events.query('points_earned>0')[['onset', 'duration','points_earned']]
    cond_gain = cond_gain.rename(index=str, columns={"points_earned": "modulation"})
    cond_gain['trial_type'] =  "gain"

    cond_loss = cur_events.query('points_earned<0')[['onset', 'duration','points_earned']]
    cond_loss = cond_loss.rename(index=str, columns={"points_earned": "modulation"})
    cond_loss['trial_type'] =  "loss"

    cond_junk = cur_events.query('response == 0')[['onset', 'duration']]
    cond_junk['modulation'] = 1
    cond_junk['trial_type'] = "junk"

    formatted_events = pd.concat([cond_m1, cond_m2, cond_m3, cond_m4, cond_m1_rt, cond_m2_rt, cond_m3_rt, cond_m4_rt, cond_gain, cond_loss, cond_junk], ignore_index=True)

    formatted_events = formatted_events.sort_values(by='onset')

    formatted_events = formatted_events[['onset', 'duration', 'trial_type', 'modulation']].reset_index(drop=True)

    #process confounds
    #['X','Y','Z','RotX','RotY','RotY','<-firsttemporalderivative','stdDVARs','FD','scrub']
    cur_confounds = pd.read_csv(os.path.join(data_loc,"derivatives/fmriprep_1.3.0/fmriprep/sub-%s/func/sub-%s_task-machinegame_run-%s_desc-confounds_regressors.tsv"%(subnum, subnum, runnum)), sep='\t')

    formatted_confounds = cur_confounds[['trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z']]
    add_transform(formatted_confounds, type="sq")
    add_transform(formatted_confounds, type="td")
    formatted_confounds[['std_dvars', 'framewise_displacement']] = cur_confounds[['std_dvars', 'framewise_displacement']]
    formatted_confounds['std_dvars'].iloc[0] = 0
    formatted_confounds['framewise_displacement'].iloc[0] = 0
    formatted_confounds['scrub'] = np.where(formatted_confounds.framewise_displacement>0.5,1,0)

    #define GLM parmeters
    fmri_glm = FirstLevelModel(t_r=cur_img_tr,
                           noise_model='ar1',
                           standardize=False,
                           hrf_model='spm + derivative',
                           drift_model='cosine',
                           smoothing_fwhm=5)

    #fit glm to run image using run events
    fmri_glm = fmri_glm.fit(fmri_img, events = formatted_events, confounds = formatted_confounds)

    #OUTPUTs:
    #Design matrix image
    design_matrix = fmri_glm.design_matrices_[0]
    plot_design_matrix(design_matrix, output_file=os.path.join(outdir, 'sub-%s_run-%s_level1_design_matrix.png' %(subnum, runnum)))

    #Design matrix itself

    #Model object that will be fed into level2s

    #Whatever randomise needs

    #Contrast zmaps

    #Whatever else Ian is saving
