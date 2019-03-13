import os
import sys
from pyxnat_config import xnat

(project, subject, experiment) = sys.argv[1:]

proj = xnat.select.project(project)
subj = proj.subject(subject)
exp = subj.experiment(experiment)
scan = "T1"
path = "/data"

uploads = [{'resource': 'XFORM_MATRIX', 'content': 'MNI to subject space transform',
            'file_name': 'xform_MNI2subject.txt', 'type': 'MNI to subject space transform', 'format': 'TXT'},
           {'resource': 'REGISTERED_ATLAS', 'content': 'atlas in subject space',
            'file_name': 'HarvOx-cort_subjectSpace.nii.gz', 'type':'atlas in subject space', 'format': 'NIFTI'},
           {'resource': 'REGISTERED_VOL', 'content': 'MNI template in subject space',
            'file_name': 'struct_MNI2subject.nii.gz', 'type': 'MNI template in subject space', 'format': 'NIFTI'}
           ]

for upload in uploads:
    exp.scan(scan).resource(upload['resource']).file(upload['file_name']).insert(
        os.path.join(path, upload['file_name']), **upload)

