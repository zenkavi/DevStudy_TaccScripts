import nibabel as nib
import nistats
import numpy as np
import os
import pandas as pd

data_loc = os.environ['DATA_LOC']
home = os.environ['HOME']

#each point in this image is the mean z-score for the regression coefficient between the convolved m1 regressor and BOLD activity across the 6 runs
sub_img_file = data_loc+'/derivatives/nistats/level_2/sub-100009/contrasts/sub-100009_m1.nii.gz'
sub_img = nib.load(sub_img_file)
sub_img_data = sub_img.get_data().astype('float32')

#question: do the average (?) z-scores from ROIs (one per subject) correlate with drift rates differently for each age group?
roi_img_file = data_loc+'/derivatives/fslmaths/ACC_bin.nii.gz'
roi_img = nib.load(roi_img_file)
roi_img_data = roi_img.get_data().astype('bool')

n_vox = np.argwhere(roi_img_data==True).shape[0]
print("***********************************************")
print("Extracting z-values for %s voxels"%(str(n_vox)))
print("***********************************************")

voxs = np.argwhere(roi_img_data==True)
sub_zvals = []
for v in voxs:
    x = v[0]
    y = v[1]
    z = v[2]
    v_zval = sub_img_data[x,y,z]
    sub_zvals.append(v_zval)

m_zvals = np.mean(sub_zvals)
std_zvals = np.std(sub_zvals)