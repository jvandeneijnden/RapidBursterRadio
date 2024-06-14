############### IMAGING ################
#                                      #
# USE: run this file in CASA using     #
# execfile('imaging_average.py')       #
# VERSION: CASA v6.5.5.21              #
#                                      #
########################################

### This file can be used to produce the time averaged images shown in the paper. 
### The .fits images can plotted using the accompanying Jupyter Notebook.

### Define the measurement set, that has now been flagged and calibrated.

mylabel='RB_Cband'					
myvis=mylabel+'_hs.ms'

### Split of two versions, containing only the calibrated target data with two different UV cuts:

split(vis=myvis, outputvis=mylabel+'.split.UVcut_max20klambda.ms', datacolumn='corrected', field='1', uvrange='<20klambda')

split(vis=myvis, outputvis=mylabel+'.split.UVcut_min20klambda.ms', datacolumn='corrected', field='1', uvrange='>20klambda')

### Image the two split-off measurement sets:

myvis=mylabel+'.split.UVcut_max20klambda.ms'

tclean(vis=myvis, imagename=mylabel+'.UVcut_max20klambda.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.040 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0)

myvis=mylabel+'.split.UVcut_min20klambda.ms'

tclean(vis=myvis, imagename=mylabel+'.UVcut_min20klambda.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.040 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0)

### Also split off a third measurement set that contains the uvcut that we will use in the rest of the analysis, with again only the calibrated target data, to be used in the following scripts.

myvis=mylabel+'_hs.ms'

split(vis=myvis, outputvis='RapidBurster_Calibrated_TargetOnly.ms', datacolumn='corrected', field='1', uvrange='>3.5klambda')

### Use that image to create a full field image:

myvis='RapidBurster_Calibrated_TargetOnly.ms'

tclean(vis=myvis, imagename='fullfield.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.030 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0)

### Finally, export the .image files from casa to .fits files for further plotting. Note the dropdeg=True, which removes the frequency and stokes axis and allows for aplpy plotting.

exportfits(imagename=mylabel+'.UVcut_max20klambda.im1.image', fitsimage='RB_Cband.UVcut_max20klambda.im1.image.dropdeg.fits', dropdeg=True)
exportfits(imagename=mylabel+'.UVcut_min20klambda.im1.image', fitsimage='RB_Cband.UVcut_min20klambda.im1.image.dropdeg.fits', dropdeg=True)
exportfits(imagename='fullfield.im1.image', fitsimage='images_per_scan.ALL.im1.fits', dropdeg=True)

### The last one has a different name to make it easier to plot the image together with those from the individual scans, that are generated later on.
