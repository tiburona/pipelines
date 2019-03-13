#!/usr/bin/env bash

# Download the files.  Positional arguments: project identifier, subject identifier, experiment identifier
python /usr/src/flirt/pyxnat_download.py $1 $2 $3

# Run the FLIRT command.
cd /data
flirt -in MNI152_T1_1.5mm.nii.gz -ref scan.nii.gz -out struct_MNI2subject.nii.gz -omat xform_MNI2subject.txt -dof 12
flirt -ref scan.nii.gz -in HarvardOxford-cortl-maxprob-thr0-1mm.nii.gz -applyxfm -init xform_MNI2subject.txt -out HarvOx-cort_subjectSpace.nii.gz -noresample

# Upload the files to XNAT.  Positional arguments: project identifier, subject identifier, experiment identifier
cd /usr/src/flirt
python /usr/src/flirt/pyxnat_upload.py $1 $2 $3