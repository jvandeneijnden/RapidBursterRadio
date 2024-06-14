########## ANALYSIS PER SCAN ###########
#                                      #
# USE: run this file in CASA using     #
# execfile('analysis_per_scan.py')     #
# VERSION: CASA v6.5.5.21              #
#                                      #
########################################

### This script fits the flux density of the Rapid Burster and the check source at different time resolutions.
### It prints the outcome in the casa terminal. These light curve are separately plotted using a Jupyter Notebook.

### In addition, it creates images for each scan at the end. 

### First, perform the uv plane analysis for the Rapid Burster, using the .ms we created in the previous step:

myvis = 'RB_uvsub.phaseshifted.ms'

### Measure the target field scan numbers, as well as start and end mjds of the scans:

output = listobs(myvis) 
scans = []
begins = []
ends = []
for k in range(5*len(output)):
	try:
		scan_ID = output['scan_'+str(k)]['0']['scanId']
		scans.append(scan_ID)
			
		begins.append(output['scan_'+str(k)]['0']['BeginTime'])
		ends.append(output['scan_'+str(k)]['0']['EndTime'])
	except KeyError:
		pass

### We will perform the analysis for three time resolutions:

Nperscan_list = [1., 4., 8.]

# Perform the analysis for 1, 4, and 8 measurements per scan:
for Nperscan in Nperscan_list:

	fluxes_perbin = []
	bins = []
	times = []
	
	# Loop over the scans:
	for k in range(len(scans)):

		# Calculate the size of each bins:
		dMJD = ends[k] - begins[k]
		bin_size = dMJD / Nperscan

		# Loop over the bins:
		for i in range(int(Nperscan)):
			
			# Save the bin number
			bins.append(1+Nperscan*k+i)	

			# Save the middle point in time for the bin:
			bin_begin = qa.time(qa.quantity(begins[k]+i*bin_size, 'd'),form='ymd')[0]
			bin_end = qa.time(qa.quantity(begins[k]+(i+1)*bin_size, 'd'),form='ymd')[0]

			times.append(begins[k]+(i+0.5)*bin_size)

			# Perform the uvmodelfit
			uvmodelfit(vis=myvis, niter=3, comptype ='P', sourcepar =[1.0e-3,0.0,0.0], varypar=[True,False,False], outfile='componentlist'+str(i)+'_'+str(k)+'.cl', timerange=bin_begin+'~'+bin_end)

			# Open the fit output to save the flux:
			cl.open('componentlist'+str(i)+'_'+str(k)+'.cl')
			fit = cl.getcomponent(0)
			flux = fit['flux']['value'][0]
			cl.close()
	
			# Append the flux:
			fluxes_perbin.append(flux)

	# Print the output for this time resolution:
	print("-----------------------------------------")
	print("Rapid Burster:", Nperscan, "bins per scan")
	print(bins)
	print(times)
	print(fluxes_perbin)
	print("-----------------------------------------")

### Now, repeat the analysis for the check source: 

myvis = 'RB_uvsub_CHECKSOURCE.phaseshifted.ms'

### We can go straight into the analysis, since the scans are the same:

Nperscan_list = [1., 4.]

# Perform the analysis for 1 and 4 measurements per scan:
for Nperscan in Nperscan_list:

	fluxes_perbin = []
	bins = []
	times = []
	
	# Loop over the scans:
	for k in range(len(scans)):

		# Calculate the size of each bins:
		dMJD = ends[k] - begins[k]
		bin_size = dMJD / Nperscan

		# Loop over the bins:
		for i in range(int(Nperscan)):
			
			# Save the bin number
			bins.append(1+Nperscan*k+i)	

			# Save the middle point in time for the bin:
			bin_begin = qa.time(qa.quantity(begins[k]+i*bin_size, 'd'),form='ymd')[0]
			bin_end = qa.time(qa.quantity(begins[k]+(i+1)*bin_size, 'd'),form='ymd')[0]

			times.append(begins[k]+(i+0.5)*bin_size)

			# Perform the uvmodelfit
			uvmodelfit(vis=myvis, niter=3, comptype ='P', sourcepar =[1.0e-3,0.0,0.0], varypar=[True,False,False], outfile='componentlist'+str(i)+'_'+str(k)+'.cl', timerange=bin_begin+'~'+bin_end)

			# Open the fit output to save the flux:
			cl.open('componentlist'+str(i)+'_'+str(k)+'.cl')
			fit = cl.getcomponent(0)
			flux = fit['flux']['value'][0]
			cl.close()
	
			# Append the flux:
			fluxes_perbin.append(flux)

	# Print the output for this time resolution:
	print("-----------------------------------------")
	print("Check source:", Nperscan, "bins per scan ")
	print(bins)
	print(times)
	print(fluxes_perbin)
	print("-----------------------------------------")

### Finally, create the images per scan. For this, we use the full dataset, without any uv subtraction:

myvis = 'RapidBurster_Calibrated_TargetOnly.ms'

# Looping over each scan:

for scan in scans:
	SCAN = str(scan)
	
	tclean(vis=myvis, imagename='images_per_scan.'+SCAN+'.im1', nterms=1, stokes='I', deconvolver='hogbom', specmode='mfs', niter=2000, gain=0.1, threshold='0.030 mJy', interactive=False, cycleniter=100, imsize=2048, cell='0.7arcsec', weighting='briggs', robust=0.0, scan=SCAN)
	
	exportfits(imagename='images_per_scan.'+SCAN+'.im1.image', exportfits='images_per_scan.'+SCAN+'.im1.fits', dropdeg=True)

















