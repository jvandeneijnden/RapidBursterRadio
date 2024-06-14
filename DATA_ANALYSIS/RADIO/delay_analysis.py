######### ANALYSIS WITH DELAYS #########
#                                      #
# USE: run this file in CASA using     #
# execfile('delay_analysis.py')        #
# VERSION: CASA v6.5.5.21              #
#                                      #
########################################

### This script will calculate the flux of the burst and non-burst intervals, 
### taking into account increasingly larger shifts up to 900 seconds (15 minutes).

import numpy as np
import os

### Define the start and durations of the bursts. These are measured in seconds since the start of the Swift observation, in seconds

burst_starts = np.asarray([67.5, 308.5, 395.5, 480.5,544.5,639.5,743.5,818.5,897.5,993.5,1346.5,5732.5,5773.5,5838.5,6087.5,6218.5,6451.5,6525.5,6557.5,6578.5,6602.5,6624.5,6880.5,7127.5,7159.5,7180.5,7198.5])
burst_T = np.asarray([43., 19., 22., 16., 23., 25., 21., 26., 24., 56., 61., 13., 19., 39., 34., 48., 22., 11.,  5.,  7.,  7., 40., 39., 10.,  5.,  5., 41.])

### Defining the start of the Swift and VLA observations on target in MJD:

MJD0_Swift = 58927.5086025
MJD0_VLAscan1 = 58927.50821759259

### Defining the measurement set: 

myvis = 'RB_uvsub.phaseshifted.ms'

### Defining the correct shifts, in mjd, and the converting the burst start times and durations to MJD:

fluxes_burst = []
fluxes_nonburst = []

shifts_seconds = np.linspace(0, 15*60, 20, endpoint=True)
sec_per_mjd = 86400.
shifts_mjd = shifts_seconds / sec_per_mjd

bursts_mjd = MJD0_Swift + burst_starts / sec_per_mjd
bursts_T_mjd = burst_T / sec_per_mjd

### Looping over the shifts.
### For each time shift, we calculate a burst and non-burst flux density, and save that. 

for SHIFT in shifts_mjd:

	### Analyse the shifted burst times: start by creating a time selection:

	time_selection = ''

	for i in range(len(bursts_mjd)):
		begin = qa.time(qa.quantity(bursts_mjd[i]+SHIFT, 'd'),form='ymd')[0]
		end = qa.time(qa.quantity(bursts_mjd[i]+SHIFT+bursts_T_mjd[i], 'd'),form='ymd')[0]
	
		time_selection = time_selection + begin + '~' + end + ','

	time_selection = time_selection[:-1]
	
	### Check if the fit has not been performed (to save time); if not, perform the uvmodelfit:

	if not os.path.exists('./componentlist_burst_'+str(int(SHIFT*sec_per_mjd))+'.cl'):
		uvmodelfit(vis=myvis, niter=3, comptype ='P', sourcepar =[1.0e-3,0.0,0.0], varypar=[True,False,False], outfile='componentlist_burst_'+str(int(SHIFT*sec_per_mjd))+'.cl', timerange=time_selection)

	### Save the flux:

	cl.open('componentlist_burst_'+str(int(SHIFT*sec_per_mjd))+'.cl')
	fit = cl.getcomponent(0)
	flux = fit['flux']['value'][0]
	cl.close()
	
	fluxes_burst.append(flux)

	### Repeat these steps for the non-burst times (note the difference in the definition of the begin and ends when creating the time selection):

	time_selection = ''

	begin = qa.time(qa.quantity(MJD0_VLAscan1+SHIFT, 'd'),form='ymd')[0]
	end = qa.time(qa.quantity(bursts_mjd[0]+SHIFT, 'd'),form='ymd')[0]

	time_selection = time_selection + begin + '~' + end + ','
	
	for i in range(1,len(bursts_mjd)):
		begin = qa.time(qa.quantity(bursts_mjd[i-1]+bursts_T_mjd[i-1]+SHIFT, 'd'),form='ymd')[0]
		end = qa.time(qa.quantity(bursts_mjd[i]+SHIFT, 'd'),form='ymd')[0]
	
		time_selection = time_selection + begin + '~' + end + ','

	time_selection = time_selection[:-1]
	
	if not os.path.exists('./componentlist_nonburst_'+str(int(SHIFT*sec_per_mjd))+'.cl'):
		uvmodelfit(vis=myvis, niter=3, comptype ='P', sourcepar =[1.0e-3,0.0,0.0], varypar=[True,False,False], outfile='componentlist_nonburst_'+str(int(SHIFT*sec_per_mjd))+'.cl', timerange=time_selection)

	cl.open('componentlist_nonburst_'+str(int(SHIFT*sec_per_mjd))+'.cl')
	fit = cl.getcomponent(0)
	flux = fit['flux']['value'][0]
	cl.close()
	
	fluxes_nonburst.append(flux)

### Print the calculated values:

print(shifts_seconds)
print(fluxes_burst)
print(fluxes_nonburst)


