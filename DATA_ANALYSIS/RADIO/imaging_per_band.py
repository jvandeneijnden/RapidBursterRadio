############### IMAGING ################
#                                      #
# USE: run this file in CASA using     #
# execfile('imaging_per_band.py')      #
# VERSION: CASA v6.5.5.21              #
#                                      #
########################################

### This file can be used to produce the images in the two sub-bands of the data.
### From those images, we then measure the flux densities and spectral index.

### Note that 

myvis='RapidBurster_Calibrated_TargetOnly.ms'

### Image spectral windows: 2~17 and 18~33 separately:

tclean(vis=myvis, imagename='ImagePerBand.spw2_17.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.030 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0, spw='2~17')

tclean(vis=myvis, imagename='ImagePerBand.spw18_33.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.030 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0, spw='18~33')

### Determine the flux densities per image separately: for 2~17 (4-6 GHz)

imfit("ImagePerBand.spw2_17.im1.image", estimates='estimates2_17.txt', box='1021, 1000, 1029, 1016')

### From the logger, we see that the flux = 63.3 uJy
### In the image, using imview, we measure that the RMS = 8 uJy

### Determine the flux densities per image separately: for 18~33 (6-8 GHz)

imfit("ImagePerBand.spw18_33.im1.image", estimates='estimates18_33.txt', box='1021, 1000, 1029, 1016')

### From the logger, we see that the flux = 55.1 uJy
### In the image, using imview, we measure that the RMS = 8 uJy

### Combined, these measurements imply alpha = -0.4+/-1.3


