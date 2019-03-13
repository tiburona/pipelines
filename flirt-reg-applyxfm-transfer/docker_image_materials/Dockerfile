
FROM brainlife/fsl

RUN mkdir /usr/src/flirt
RUN mkdir /data

COPY container-workflow.sh pyxnat_download.py pyxnat_upload.py pyxnat_config.py xnat.cfg /usr/src/flirt/

WORKDIR /usr/src/flirt

COPY MNI152_T1_1.5mm.nii.gz HarvardOxford-cortl-maxprob-thr0-1mm.nii.gz /data/

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN pip install pyxnat