    #!/usr/bin/python
import os
import glob
import nibabel as nib
import re
from argparse import ArgumentParser

#Usage: python make_l3_fsfs.py -m 1

parser = ArgumentParser()
parser.add_argument("-m", "--model_number", help="model number")
parser.add_argument('-e','--evs', nargs='+', help='EVs', default = ['m1', 'm2', 'm3', 'm4', 'm1_rt', 'm2_rt', 'm3_rt', 'm4_rt', 'pe_lv', 'pe_hv', 'junk'])
args = parser.parse_args()

model_number = args.model_number
evs = args.evs

try:
    data_loc = os.environ['DATA_LOC']
    server_scripts = os.environ['SERVER_SCRIPTS']
except KeyError:
    os.system('source /oak/stanford/groups/russpold/users/zenkavi/DevStudy_ServerScripts/setup/dev_study_env.sh')
    data_loc = os.environ['DATA_LOC']
    server_scripts = os.environ['SERVER_SCRIPTS']

copenums = {'m1': "cope1.feat", 'm2': "cope2.feat", 'm3':"cope3.feat", 'm4':"cope4.feat", 'm1_rt':"cope5.feat", 'm2_rt':"cope6.feat", 'm3_rt':"cope7.feat", 'm4_rt':"cope8.feat", 'pe_lv':"cope9.feat", 'pe_hv':"cope10.feat", 'junk':"cope11.feat"}

for ev in evs:
  print("Making design file for model %s EV %s"%(model_number, ev))
  replacements = {"EVN": ev, "COPENUM": copenums.get(ev)}
  if not os.path.exists("%s/derivatives/level_3/model%s"%(data_loc, model_number)):
      os.makedirs(os.path.join("%s/derivatives/level_3/model%s/"%(data_loc, model_number)))
  with open("%s/level_3/model%s/template_l3_model%s.fsf"%(server_scripts, model_number, model_number)) as infile:
    with open("%s/derivatives/level_3/model%s/%s.fsf"%(data_loc, model_number, ev), 'w') as outfile:
        for line in infile:
          for src, target in replacements.items():
            line = line.replace(src, target)
          outfile.write(line)

#ls /oak/stanford/groups/russpold/data/ds000054/0.0.4/derivatives/level_2/sub*/model1/*.gfeat/cope1.feat/stats/cope1.nii.gz
