Notes on `FSL for task fMRI` series from mumfordbrainstats
==========================================================

- **[DONE]** Convert DICOM to NIfTI  

- QA  
  - Check if all files exist (Notes from BIDS report)  
    Missing behavioral data for all runs of sub-100060 **[MOVED TO SOURCEDATA]**  
    Missing behavioral data for all runs of sub-200027 **[MOVED TO SOURCEDATA]**  
    Missing behavioral data for all runs of sub-200081 **[MOVED TO SOURCEDATA]**  
    Missing behavioral data for all runs of sub-304228 **[MOVED TO SOURCEDATA]**  
    Missing behavioral data for all runs of sub-308023 **[MOVED TO SOURCEDATA]**  
    Missing behavioral data for all runs of sub-406989 **[MOVED TO SOURCEDATA]**  
    Missing behavioral data for all runs of sub-411236 **[MOVED TO SOURCEDATA]**  
    Missing behavioral data for run 6 for sub-100110  
  - Check BOLD volumes with volumes !=216:  
    sub-100103/func/sub-100103_task-machinegame_run-03_bold.nii.gz,42  
    sub-100110/func/sub-100110_task-machinegame_run-06_bold.nii.gz,161  
    sub-100188/func/sub-100188_task-machinegame_run-04_bold.nii.gz,153  
    sub-100215/func/sub-100215_task-machinegame_run-01_bold.nii.gz,141  
    sub-100241/func/sub-100241_task-machinegame_run-04_bold.nii.gz,11  
    sub-306065/func/sub-306065_task-machinegame_run-01_bold.nii.gz,148  
    sub-406989/func/sub-406989_task-machinegame_run-01_bold.nii.gz,131 **[MOVED TO SOURCEDATA]**  
  - Check fmap volumes != 96,96,56 (voxels):
    sub-406989/fmap/sub-406989_magnitude1.nii.gz, This file has the dimensions: 92,96,56 (voxels). **[MOVED TO SOURCEDATA]**  
    sub-406989/fmap/sub-406989_magnitude2.nii.gz, This file has the dimensions: 92,96,56 (voxels). **[MOVED TO SOURCEDATA]**  
    sub-406989/fmap/sub-406989_phasediff.nii.gz, This file has the dimensions: 92,96,56 (voxels). **[MOVED TO SOURCEDATA]**
  - Check anatomical != 0.80mm x 0.80mm x 0.80mm  
    sub-406989/anat/sub-406989_T1w.nii.gz, This file has the resolution: 0.80mm x 0.85mm x 0.85mm. **[MOVED TO SOURCEDATA]**  

- Skull script structural images
- QA
- Functionals preprocessing
  - Trim volumes from beginning
  - Fix orientation issues
  - Assess motion
- QA
- Level 1 analyses
- QA
- Level 2 analyses
- QA
- Group level analyses
- QA