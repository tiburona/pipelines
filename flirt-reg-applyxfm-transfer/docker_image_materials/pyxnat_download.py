import os
import sys
from pyxnat_config import xnat

(project, subject, experiment) = sys.argv[1:]

print 'foo'

ref_file = os.path.join('/projects', project, 'subjects', subject, 'experiments', experiment, 'scans', 'T1',
                         'resources/NIFTI/files/scan.nii.gz')

xnat.select(ref_file).get('/data/scan.nii.gz')

