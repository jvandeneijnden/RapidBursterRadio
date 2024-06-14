########### UV SUBTRACTION #############
#                                      #
# USE: run this file in CASA using     #
# execfile('uv_subtraction.py')        #
# VERSION: CASA v6.5.5.21              #
#                                      #
########################################

### This file performs the subtraction of all other sources to prepare for the uv-plane variability analysis. 
### It also contains the explanation of how the positions and flux densities of all sources in the field were determined. 

### Making two copies of the split-off calibrated, >3.5klambda target data. One will be used to subtract all
### sources except the Rapid Burster; the other will be the same with the check source.

myvis = 'RapidBurster_Calibrated_TargetOnly.ms'

cp -r RapidBurster_Calibrated_TargetOnly.ms RB_uvsub.ms
cp -r RapidBurster_Calibrated_TargetOnly.ms RB_uvsub_CHECKSOURCE.ms

### To check the positions of all sources in the field, we make a test image of the full field:

tclean(vis=myvis, imagename='testimage.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.030 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0)

# Apart from the Rapid Burster, at the centre, there are sources within the following box coordinates (bottom left, top right; x1, y1, x2, y2, in pixels in the image):

# 680,955,692,978
# 917,1059,924,1070
# 998,1276,1006,1291
# 1006,875,1013,888
# 1031,1001,1035,1012
# 1253,803,1261,820
# 1270,909,1278,924
# 1306,1265,1317,1286
# 1440,1086,1450,1101

# The beam for this image is 6.07 arcsec, 1.98 arcsec, 2.39 degree. 
# To measure their positions, we can run the loop below, which will: fit the source in each of hose boxes, using a 30 uJy as the initial flux density estimate.
# It will then write the correct beam and estimate for the x,y coordinates of the source to a file called estimate_<number>.txt. 
# The loop will then print the command to run to measure the flux densities with the correct beam. 

boxes = ['680,955,692,978',
'917,1059,924,1070',
'998,1276,1006,1291',
'1006,875,1013,888',
'1031,1001,1035,1012',
'1253,803,1261,820',
'1270,909,1278,924',
'1306,1265,1317,1286',
'1440,1086,1450,1101']

for i in range(len(boxes)):
	x1 = float(boxes[i].split(',')[0])
	y1 = float(boxes[i].split(',')[1])
	x2 = float(boxes[i].split(',')[2])
	y2 = float(boxes[i].split(',')[3])

	xest = (x1+x2)/2.
	yest = (y1+y2)/2.

	estimates = '3e-5, '+str(xest)+', '+str(yest)+', 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp'
	filename = open('estimates'+str(i)+'.txt', 'w')
	filename.write(estimates)
	filename.close()
	Command = "imfit('testimage.im1.image', estimates='estimates"+str(i)+".txt', box='"+boxes[i]+"')"
	print(Command)
	
# That gives, in the estimate_<number>.txt files:
# 3e-5, 686.0, 966.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp
# 3e-5, 920.5, 1064.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp
# 3e-5, 1002.0, 1283.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp
# 3e-5, 1009.5, 881.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp
# 3e-5, 1033.0, 1006.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp
# 3e-5, 1257.0, 811.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp
# 3e-5, 1274.0, 916.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp
# 3e-5, 1311.5, 1275.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp
# 3e-5, 1445.0, 1093.5, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp

# and the commands:

imfit('testimage.im1.image', estimates='estimates0.txt', box='680,955,692,978')

# With as output in the logger: 
# 2024-02-19 11:25:21 INFO imfit	       --- ra:    17:33:43.5019 +/- 0.0018 s (0.0220 arcsec along great circle)
# 2024-02-19 11:25:21 INFO imfit	       --- dec: -033.23.48.3268 +/- 0.1921 arcsec
# 2024-02-19 11:25:21 INFO imfit	       --- Integrated:   155.5 +/- 6.6 uJy
 imfit('testimage.im1.image', estimates='estimates1.txt', box='917,1059,924,1070')

# 2024-02-19 11:27:34 INFO imfit	       --- ra:    17:33:30.4384 +/- 0.0028 s (0.0352 arcsec along great circle)
# 2024-02-19 11:27:34 INFO imfit	       --- dec: -033.22.41.4064 +/- 0.3080 arcsec
# 2024-02-19 11:27:34 INFO imfit	       --- Integrated:   42.5 +/- 2.9 uJy

imfit('testimage.im1.image', estimates='estimates2.txt', box='998,1276,1006,1291')

# 2024-02-19 11:27:59 INFO imfit	       --- ra:    17:33:25.9230 +/- 0.0047 s (0.0594 arcsec along great circle)
# 2024-02-19 11:27:59 INFO imfit	       --- dec: -033.20.08.9052 +/- 0.5197 arcsec
# 2024-02-19 11:27:59 INFO imfit	       --- Integrated:   40.1 +/- 4.6 uJy

imfit('testimage.im1.image', estimates='estimates3.txt', box='1006,875,1013,888')

# 2024-02-19 11:28:25 INFO imfit	       --- ra:    17:33:25.5078 +/- 0.0046 s (0.0575 arcsec along great circle)
# 2024-02-19 11:28:25 INFO imfit	       --- dec: -033.24.48.9702 +/- 0.5030 arcsec
# 2024-02-19 11:28:25 INFO imfit	       --- Integrated:   31.5 +/- 3.5 uJy

imfit('testimage.im1.image', estimates='estimates4.txt', box='1031,1001,1035,1012')

# 2024-02-19 11:29:02 INFO imfit	       --- ra:    17:33:24.1118 +/- 0.0114 s (0.1424 arcsec along great circle)
# 2024-02-19 11:29:02 INFO imfit	       --- dec: -033.23.21.4479 +/- 1.2456 arcsec
# 2024-02-19 11:29:02 INFO imfit	       --- Integrated:   18.7 +/- 5.2 uJy

imfit('testimage.im1.image', estimates='estimates5.txt', box='1253,803,1261,820')

# 2024-02-19 11:29:24 INFO imfit	       --- ra:    17:33:11.6615 +/- 0.0018 s (0.0223 arcsec along great circle)
# 2024-02-19 11:29:24 INFO imfit	       --- dec: -033.25.38.4380 +/- 0.1948 arcsec
# 2024-02-19 11:29:24 INFO imfit	       --- Integrated:   77.6 +/- 3.4 uJy

imfit('testimage.im1.image', estimates='estimates6.txt', box='1270,909,1278,924')

# 2024-02-19 11:29:43 INFO imfit	       --- ra:    17:33:10.6993 +/- 0.0026 s (0.0322 arcsec along great circle)
# 2024-02-19 11:29:43 INFO imfit	       --- dec: -033.24.25.5417 +/- 0.2821 arcsec
# 2024-02-19 11:29:43 INFO imfit	       --- Integrated:   80.4 +/- 5.0 uJy

imfit('testimage.im1.image', estimates='estimates7.txt', box='1306,1265,1317,1286')

# 2024-02-19 11:30:02 INFO imfit	       --- ra:    17:33:08.5859 +/- 0.0022 s (0.0280 arcsec along great circle)
# 2024-02-19 11:30:02 INFO imfit	       --- dec: -033.20.13.6225 +/- 0.2449 arcsec
# 2024-02-19 11:30:02 INFO imfit	       --- Integrated:   127.3 +/- 6.9 uJy

imfit('testimage.im1.image', estimates='estimates8.txt', box='1440,1086,1450,1101')  # 2024-02-19 11:30:26 INFO imfit	       --- ra:    17:33:01.1628 +/- 0.0018 s (0.0221 arcsec along great circle)
# 2024-02-19 11:30:26 INFO imfit	       --- dec: -033.22.21.7364 +/- 0.1931 arcsec
# 2024-02-19 11:30:26 INFO imfit	       --- Integrated:   96.1 +/- 4.1 uJy
 ### Based on these fit outcomes, we can define the following model components:

cl.addcomponent(flux=155.5e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:43.5019 -33.23.48.3268', freq='6.0GHz')
cl.addcomponent(flux=42.5e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:30.4384 -33.22.41.4064', freq='6.0GHz')
cl.addcomponent(flux=40.1e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:25.9230 -33.20.08.9052', freq='6.0GHz')
cl.addcomponent(flux=31.5e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:25.5078 -33.24.48.9702', freq='6.0GHz')
cl.addcomponent(flux=18.7e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:24.1118 -33.23.21.4479', freq='6.0GHz')
cl.addcomponent(flux=77.6e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:11.6615 -33.25.38.4380', freq='6.0GHz')
cl.addcomponent(flux=80.4e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:10.6993 -33.24.25.5417', freq='6.0GHz')
cl.addcomponent(flux=127.3e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:08.5859 -33.20.13.6225', freq='6.0GHz')
cl.addcomponent(flux=96.1e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:01.1628 -33.22.21.7364', freq='6.0GHz')

### And rename the model to othersources.cl:

cl.rename('othersources.cl')
cl.close()

### We will then subtract this model from the correct copy of the measurement set:

myvis='RB_uvsub.ms'
ft(vis=myvis, complist='othersources.cl', usescratch=True)
uvsub(vis=myvis)

### We can create an image to check if it worked:

tclean(vis=myvis, imagename='testimage.uvsubbed.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.030 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0)

### Indeed, comparing with the original 'testimage' (made above), we can see that all other sources are removed. We can also measure the position and flux density of the Rapid Burster itself:

estimates = '5e-5, 1024.0, 1009.0, 6.07 arcsec, 1.98 arcsec, 2.39 deg, abp'
filename = open('estimatesRB.txt', 'w')
filename.write(estimates)
filename.close()
imfit('testimage.uvsubbed.im1.image', estimates='estimatesRB.txt', box='1020,1001,1028,1017')

# 2024-02-19 15:05:23 INFO imfit	       --- ra:    17:33:24.6124 +/- 0.0031 s (0.0390 arcsec along great circle)
# 2024-02-19 15:05:23 INFO imfit	       --- dec: -033.23.20.1488 +/- 0.3411 arcsec
# 2024-02-19 11:30:26 INFO imfit	       --- Integrated:   58.1 +/- 5.5 uJy

### Using this position, we can now apply a phase shift to this measurement set:

phaseshift(vis=myvis, outputvis='RB_uvsub.phaseshifted.ms', phasecenter='J2000 17:33:24.6124 -33.23.20.1488')

### With that, we have created a measurement set with only the Rapid Burster, at the phase centre. 

### We will now repeat this analysis for the check source:
### The main difference is that here, when we create the source model, we remove the check source and add the Rapid Burster:

cl.addcomponent(flux=58.1e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:24.6122 -33.23.20.1392', freq='6.0GHz')
cl.addcomponent(flux=155.5e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:43.5019 -33.23.48.3268', freq='6.0GHz')
cl.addcomponent(flux=42.5e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:30.4384 -33.22.41.4064', freq='6.0GHz')
cl.addcomponent(flux=40.1e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:25.9230 -33.20.08.9052', freq='6.0GHz')
cl.addcomponent(flux=31.5e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:25.5078 -33.24.48.9702', freq='6.0GHz')
cl.addcomponent(flux=18.7e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:24.1118 -33.23.21.4479', freq='6.0GHz')
cl.addcomponent(flux=77.6e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:11.6615 -33.25.38.4380', freq='6.0GHz')
cl.addcomponent(flux=127.3e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:08.5859 -33.20.13.6225', freq='6.0GHz')
cl.addcomponent(flux=96.1e-6, fluxunit='Jy',shape='point', dir='J2000 17:33:01.1628 -33.22.21.7364', freq='6.0GHz')

### And rename the model to othersources_CHECKSOURCE.cl:

cl.rename('othersources_CHECKSOURCE.cl')
cl.close()

### applying it to the correct ms file and phase shift to the position of the check source:

myvis='RB_uvsub_CHECKSOURCE.ms'
ft(vis=myvis, complist='othersources_CHECKSOURCE.cl', usescratch=True)
uvsub(vis=myvis)

phaseshift(vis=myvis, outputvis='RB_uvsub_CHECKSOURCE.phaseshifted.ms', phasecenter='J2000 17:33:10.6993 -33.24.25.5417')

### We can similarly test what this looks like:

myvis='RB_uvsub_CHECKSOURCE.phaseshifted.ms'
tclean(vis=myvis, imagename='checksource_phaseshifted.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.030 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0)

### Again, that removed all sources except the check source, which is now at the phase centre. 

### These two files will then be used for the uv-plane variability analysis. 






 