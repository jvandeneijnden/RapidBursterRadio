[![DOI](https://zenodo.org/badge/815022389.svg)](https://zenodo.org/doi/10.5281/zenodo.12806381)

# Analysis reproduction repository for "The variable radio jet of the accreting neutron star the Rapid Burster"

![Light curves](NOTEBOOKS/Figure4.png?raw=true "Light curves")

## Based on Van den Eijnden, Robins, Sharma et al. (2024), MNRAS accepted.
The full paper, included updated versions can be found on https://arxiv.org/abs/2405.19827 (open access) and is included in this repository in the PAPER folder. 

This reproduction repository contains the following folders:

### 1) DATA_ANALYSIS: 

- XRAY_SPECTRUM: all files and a .tcl script to repeat the X-ray spectral fitting in XSpec. 
- RADIO: all scripts, with comments to explain the analysis, and instructions to repeat the various steps of the radio analysis. The scripts should be run in the correct order, starting with an uncalibrated measurement set from the NRAO data archive.

Both analysis folders contain a README with further details and explanations.

### 2) NOTEBOOKS:
 
- Images.ipynb: the notebook to reproduce the radio images in the main paper, based on the .fits versions of the .image files created by the scripts in the DATA_ANALYSIS/RADIO folder. The necessary .fits files are included.
- LxLr.ipynb: the notebook to reproduce the X-ray / radio luminosity diagram and the comparison of radio brightness with burst fluence. 
- Lightcurves.ipynb: the notebook to reproduce the light curves and perform all calculations referred to in the paper.

All notebook are commented to explain the steps and reasoning behind them.

Note that all notebooks can be run without re-performing the radio and X-ray data analysis: all necessary output from those steps is included in the repository to allow the user to repeat/build upon only these aspects of the analysis. 

Several small adjustments to Figures were made after creating (sub)plots in Python, such as combining the three panels for Figure 2 with a single color bar. Such instances are mentioned within the notebooks. 

### 3) PAPER:

This folder contains the pdf version of the paper and its LaTeX / Overleaf source files, which can similarly be accessed via https://arxiv.org/abs/2405.19827. 

### Contact and citations:

Please get in touch via email (jakobvandeneijnden.astro [at] gmail.com) or via GitHub with any questions.

If this repository is useful for your own research, in addition to citing the original paper, please consider including a note to this repository as well, for instance via its Zenodo DOI. If you use any part related to the X-ray / radio luminosity diagram, please cite the original compilation as well: https://ui.adsabs.harvard.edu/abs/2022zndo...7059313B

### Software requirements

All python analysis was performed using Python v3.10.13.

This paper used CASA v6.5.5.21 and XSPEC v12.13.0c

The notebooks were created using the following Python packages/versions:
 
- numpy v1.24.3
- matplotlib v3.7.2
- astropy v5.3
- aplpy v2.1.0
- scipy v1.10.1
