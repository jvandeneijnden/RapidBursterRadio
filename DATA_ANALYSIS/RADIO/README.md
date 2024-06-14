# Radio analysis 

This folder contains the script to analyse the VLA radio data, reproduce the images, and perform the measurements that underlie the others plots and results in the paper.

To reproduce the analyse, please follow these steps, sticking to the listed order. The python scripts are written to be run in CASA, using the execfile() command. 

1) download the UNCALIBRATED VLA measurement set: 20A-172.sb37594154.eb37978082.58927.49988386574.ms

2) perform flagging and calibration using flagging_calibration.py

3) produce the images for different uvrange cuts using imaging_average.py

4) produce images for the 5 and 7 GHz bands using imaging_per_band.py

5) perform uv-plane subtraction to prepare for further uv-plane analysis using uv_subtraction.py

6) Analyse the uv-plane and image-plane data per scan (and higher time resolution) using analysis_per_scan.py

7) Perform the delay analysis using delay_analysis.py

Each individual script contain a description of what it aims to do and how it works. The further analysis of the outputs and creation of figures based on these outputs can be reproduced using the Jupyter Notebooks in the NOTEBOOKS folder of this reproduction package.

In addition, the two .zip files contain all CASA images and CASA .cl files (component lists) that are also produced by the scripts, to compare the results. 

Note that the Jupyter Notebooks can be executed without re-performing these radio analysis steps: their folder contains all required data.

