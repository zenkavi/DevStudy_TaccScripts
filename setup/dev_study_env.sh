# change paths and modules depending on cluster
# sherlock
if [ $HOME == '/home/users/zenkavi' ]; then
  export PATH="/home1/04127/zenkavi/miniconda3/bin:$PATH"
  # export PATH=$HOME/miniconda/bin:$PATH
  # export TODO_PATH=/oak/stanford/groups/russpold/data/ds000054/todo/
  # export SERVER_SCRIPTS=/home/users/zenkavi/research/DevStudy_ServerScripts/
  # export DATA_LOC=/oak/stanford/groups/russpold/data/ds000054/0.0.1/
# tacc
else
  export PATH="/home1/04127/zenkavi/miniconda3/bin:$PATH"
  # source activate dev_study
  # export TODO_PATH=/corral-repl/utexas/poldracklab/users/zenkavi/dev_study/todo/
  # export SERVER_SCRIPTS=/corral-repl/utexas/poldracklab/users/zenkavi/dev_study/DevStudy_ServerScripts/
  # export DATA_LOC=/corral-repl/utexas/poldracklab/users/zenkavi/dev_study/data/
  # module load dcm2niix/7July2016
  # module load Rstats/3.2.1
fi
