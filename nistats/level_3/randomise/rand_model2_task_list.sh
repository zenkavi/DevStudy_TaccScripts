randomise -i $MODEL_DIR/m1/all_l2_model2_m1.nii.gz -o $MODEL_DIR/m1/rand/group_diff -d $MODEL_DIR/m1/model2_m1.mat -t $MODEL_DIR/design.con -f $MODEL_DIR/design.fts -n 1000 -T -v 5
randomise -i $MODEL_DIR/m2/all_l2_model2_m2.nii.gz -o $MODEL_DIR/m2/rand/group_diff -d $MODEL_DIR/m2/model2_m2.mat -t $MODEL_DIR/design.con -f $MODEL_DIR/design.fts -n 1000 -T -v 5
randomise -i $MODEL_DIR/m3/all_l2_model2_m3.nii.gz -o $MODEL_DIR/m3/rand/group_diff -d $MODEL_DIR/m3/model2_m3.mat -t $MODEL_DIR/design.con -f $MODEL_DIR/design.fts -n 1000 -T -v 5
randomise -i $MODEL_DIR/m4/all_l2_model2_m4.nii.gz -o $MODEL_DIR/m4/rand/group_diff -d $MODEL_DIR/m4/model2_m4.mat -t $MODEL_DIR/design.con -f $MODEL_DIR/design.fts -n 1000 -T -v 5
randomise -i $MODEL_DIR/lpe/all_l2_model2_lpe.nii.gz -o $MODEL_DIR/lpe/rand/group_diff -d $MODEL_DIR/lpe/model2_lpe.mat -t $MODEL_DIR/design.con -f $MODEL_DIR/design.fts -n 1000 -T -v 5
randomise -i $MODEL_DIR/hpe/all_l2_model2_hpe.nii.gz -o $MODEL_DIR/hpe/rand/group_diff -d $MODEL_DIR/hpe/model2_hpe.mat -t $MODEL_DIR/design.con -f $MODEL_DIR/design.fts -n 1000 -T -v 5
randomise -i $MODEL_DIR/hpe/all_l2_model2_pe.nii.gz -o $MODEL_DIR/pe/rand/group_diff -d $MODEL_DIR/pe/model2_pe.mat -t $MODEL_DIR/design.con -f $MODEL_DIR/design.fts -n 1000 -T -v 5
randomise -i $MODEL_DIR/task_on/all_l2_model2_task_on.nii.gz -o $MODEL_DIR/task_on/rand/group_diff -d $MODEL_DIR/task_on/model2_task_on.mat -t $MODEL_DIR/design.con -f $MODEL_DIR/design.fts -n 1000 -T -v 5
randomise -i $MODEL_DIR/var_sen/all_l2_model2_var_sen.nii.gz -o $MODEL_DIR/var_sen/rand/group_diff -d $MODEL_DIR/var_sen/model2_var_sen.mat -t $MODEL_DIR/design.con -n 1000 -T -v 5
randomise -i $MODEL_DIR/ev_sen/all_l2_model2_ev_sen.nii.gz -o $MODEL_DIR/ev_sen/rand/group_diff -d $MODEL_DIR/ev_sen/model2_ev_sen.mat -t $MODEL_DIR/design.con -n 1000 -T -v 5
