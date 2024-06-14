####### FLAGGING AND CALIBRATION #######
#                                      #
# USE: run this file in CASA using     #
# execfile('flagging_calibration.py')  #
# VERSION: CASA v6.5.5.21              #
#                                      #
########################################

### Define the measurement set and root for output files
# Note: the .ms file is stored in the VLA Data Archive at https://data.nrao.edu/
# and can be found most easily by searching for program 20A-172.
# Note that we will analyse the 'Basic Measurement Set', not the 'Calibrated Measurement Set'.

myvis='20A-172.sb37594154.eb37978082.58927.49988386574.ms'
mylabel='RB_Cband'

### Clear any prior calibration performed on the data

clearcal(vis=myvis)

### Standard flagging routines

flagdata(vis=myvis, autocorr=True)
flagdata(vis=myvis, mode='shadow')
flagdata(vis=myvis, mode='quack', quackinterval=3.0, quackmode='beg')
hanningsmooth(vis=myvis, datacolumn='all', outputvis=mylabel+'_hs.ms')

### Rename the measurement set we are working on

myvis=mylabel+'_hs.ms'

### Flag the setup scans and setup spectral windows

flagdata(vis=myvis,timerange='',spw='', field='', antenna='', scan='1~3')
flagdata(vis=myvis,timerange='',spw='0~1', field='', antenna='')

### Flagging RFI: selected based on visual inspection

flagdata(vis=myvis, spw='16', uvrange='<10klambda')
flagdata(vis=myvis, spw='16', antenna='ea02&ea09')
flagdata(vis=myvis, spw='16', antenna='ea08&ea09')
flagdata(vis=myvis, spw='16', antenna='ea08&ea26')
flagdata(vis=myvis, spw='16', antenna='ea09&ea22')
flagdata(vis=myvis, spw='16', antenna='ea02&ea08')
flagdata(vis=myvis, spw='18~19', antenna='ea09&ea12')
flagdata(vis=myvis, spw='18~19', antenna='ea02&ea09')
flagdata(vis=myvis, spw='33', antenna='ea22&ea28')
flagdata(vis=myvis, spw='2~5', uvrange='<5klambda')
flagdata(vis=myvis, spw='4', antenna='ea10&ea22')
flagdata(vis=myvis, spw='17', antenna='ea09&ea12')
flagdata(vis=myvis, spw='17', antenna='ea12&ea20')
flagdata(vis=myvis, spw='21', antenna='ea06&ea17')
flagdata(vis=myvis, spw='21', antenna='ea06&ea19')
flagdata(vis=myvis, spw='21', antenna='ea06&ea25')
flagdata(vis=myvis, spw='21', antenna='ea14&ea20')
flagdata(vis=myvis, spw='18~21', antenna='ea12&ea20')
flagdata(vis=myvis, spw='18~21', antenna='ea17&ea20')
flagdata(vis=myvis, spw='18~21', antenna='ea06&ea17')
flagdata(vis=myvis, spw='18~21', antenna='ea09&ea20')
flagdata(vis=myvis, spw='18~21', antenna='ea09&ea17')
flagdata(vis=myvis, spw='18~21', antenna='ea06&ea17')
flagdata(vis=myvis, spw='18~21', uvrange='<16klambda')
flagdata(vis=myvis, spw='19~21', antenna='ea04&ea07')
flagdata(vis=myvis, spw='19', antenna='ea07&ea18')
flagdata(vis=myvis, spw='19', antenna='ea15&ea16')
flagdata(vis=myvis, spw='21', antenna='ea11&ea21')
flagdata(vis=myvis, spw='28', antenna='ea09&ea12')
flagdata(vis=myvis, antenna='ea12')
flagdata(vis=myvis, spw='2', antenna='ea02&ea11')
flagdata(vis=myvis, spw='3', antenna='ea18&ea22')
flagdata(vis=myvis, spw='3', antenna='ea15&ea22')
flagdata(vis=myvis, spw='3', uvrange='<10klambda')
flagdata(vis=myvis, spw='4', scan='19')
flagdata(vis=myvis, spw='5', antenna='ea04')
flagdata(vis=myvis, spw='6', antenna='ea06&ea17')
flagdata(vis=myvis, spw='6', scan='13', uvrange='<20klambda')
flagdata(vis=myvis, spw='6', scan='15', uvrange='<20klambda')
flagdata(vis=myvis, spw='6', antenna='ea20')
flagdata(vis=myvis, spw='6', antenna='ea04&ea11')
flagdata(vis=myvis, spw='6', antenna='ea04&ea18')
flagdata(vis=myvis, spw='6', antenna='ea06&ea25')
flagdata(vis=myvis, spw='6', antenna='ea09&ea17')
flagdata(vis=myvis, spw='7~17', antenna='ea06&ea17')
flagdata(vis=myvis, spw='7~17', antenna='ea09&ea20')
flagdata(vis=myvis, spw='9~13', antenna='ea17')
flagdata(vis=myvis, spw='11', scan='15')
flagdata(vis=myvis, spw='13', scan='15')
flagdata(vis=myvis, spw='17', antenna='ea04&ea11')
flagdata(vis=myvis, spw='17', antenna='ea06&ea25')
flagdata(vis=myvis, spw='17', antenna='ea06&ea09')
flagdata(vis=myvis, spw='17', antenna='ea02&ea25')
flagdata(vis=myvis, spw='17', antenna='ea09&ea14')
flagdata(vis=myvis, spw='9~17', antenna='ea02&ea09')
flagdata(vis=myvis, spw='14~17', antenna='ea09&ea17')
flagdata(vis=myvis, spw='14~17', antenna='ea17&ea20')
flagdata(vis=myvis, spw='18', antenna='ea03&ea28')
flagdata(vis=myvis, spw='18', antenna='ea11&ea13')
flagdata(vis=myvis, spw='18', antenna='ea08&ea27')
flagdata(vis=myvis, spw='19', antenna='ea11&ea21')
flagdata(vis=myvis, spw='19', antenna='ea15&ea19')
flagdata(vis=myvis, spw='19', antenna='ea10&ea18')
flagdata(vis=myvis, spw='19', antenna='ea16&ea18')
flagdata(vis=myvis, spw='19', antenna='ea07')
flagdata(vis=myvis, spw='20', antenna='ea15&ea27')
flagdata(vis=myvis, spw='20', antenna='ea06&ea08')
flagdata(vis=myvis, spw='20', antenna='ea08&ea24')
flagdata(vis=myvis, spw='20', antenna='ea18&ea27')
flagdata(vis=myvis, spw='20', antenna='ea16&ea18')
flagdata(vis=myvis, spw='20', antenna='ea11&ea21')
flagdata(vis=myvis, spw='20', antenna='ea15&ea16')
flagdata(vis=myvis, spw='20', antenna='ea18&ea23')
flagdata(vis=myvis, spw='20', antenna='ea13&ea18')
flagdata(vis=myvis, spw='20', antenna='ea15&ea23')
flagdata(vis=myvis, spw='22~33', antenna='ea09&ea20')
flagdata(vis=myvis, spw='22~33', antenna='ea09&ea17')
flagdata(vis=myvis, spw='23~33', antenna='ea17')
flagdata(vis=myvis, spw='28', antenna='ea04')
flagdata(vis=myvis, spw='28', antenna='ea06')
flagdata(vis=myvis, spw='28', antenna='ea09')
flagdata(vis=myvis, spw='28', antenna='ea15&ea18')
flagdata(vis=myvis, spw='28', antenna='ea02&ea25')
flagdata(vis=myvis, spw='28~29', antenna='ea11&ea25')
flagdata(vis=myvis, spw='29', antenna='ea06&ea09')
flagdata(vis=myvis, spw='29', antenna='ea06&ea25')
flagdata(vis=myvis, spw='29', antenna='ea04&ea11')
flagdata(vis=myvis, spw='29', antenna='ea11&ea25')
flagdata(vis=myvis, spw='29', antenna='ea04&ea18')
flagdata(vis=myvis, spw='29', antenna='ea15&ea18')
flagdata(vis=myvis, spw='29', antenna='ea02&ea25')
flagdata(vis=myvis, spw='30', antenna='ea02&ea06')
flagdata(vis=myvis, spw='30', antenna='ea06&ea25')
flagdata(vis=myvis, spw='30', antenna='ea06&ea09')
flagdata(vis=myvis, spw='31', antenna='ea06')
flagdata(vis=myvis, spw='31', antenna='ea04&ea11')
flagdata(vis=myvis, spw='31', antenna='ea04&ea18')
flagdata(vis=myvis, spw='31', antenna='ea09&ea14')
flagdata(vis=myvis, spw='31', antenna='ea15&ea18')
flagdata(vis=myvis, spw='32', antenna='ea06&ea09')
flagdata(vis=myvis, spw='32', antenna='ea06&ea20')
flagdata(vis=myvis, spw='32', antenna='ea09&ea11')
flagdata(vis=myvis, spw='16:20~63')
flagdata(vis=myvis, spw='33:0~37')
flagdata(vis=myvis, spw='19')
flagdata(vis=myvis, spw='21:0~30')
flagdata(vis=myvis, spw='16')
flagdata(vis=myvis, spw='3:46~48')
flagdata(vis=myvis, spw='5:21~25')
flagdata(vis=myvis, spw='5:2~10')
flagdata(vis=myvis, spw='6:8~9')
flagdata(vis=myvis, spw='6:40~46')
flagdata(vis=myvis, spw='7', antenna='ea17')
flagdata(vis=myvis, spw='8', antenna='ea17')
flagdata(vis=myvis, spw='11:52~53')
flagdata(vis=myvis, spw='12:19~23')
flagdata(vis=myvis, spw='12:35~36')
flagdata(vis=myvis, spw='12:44~47')
flagdata(vis=myvis, spw='12:53~54')
flagdata(vis=myvis, spw='15:51~53')
flagdata(vis=myvis, spw='15:7~13')
flagdata(vis=myvis, spw='17:60~62')
flagdata(vis=myvis, spw='18', antenna='ea03&ea21')
flagdata(vis=myvis, spw='22', antenna='ea14&ea17')
flagdata(vis=myvis, spw='25', antenna='ea14&ea25')
flagdata(vis=myvis, spw='25', antenna='ea06&ea27')
flagdata(vis=myvis, spw='25:3~4')
flagdata(vis=myvis, spw='26', antenna='ea14&ea25')
flagdata(vis=myvis, spw='27:47~49')
flagdata(vis=myvis, spw='28', antenna='ea08&ea13')
flagdata(vis=myvis, spw='28', antenna='ea02&ea11')
flagdata(vis=myvis, spw='28', antenna='ea14&ea20')
flagdata(vis=myvis, spw='28', antenna='ea13&ea25')
flagdata(vis=myvis, spw='29:35~38')
flagdata(vis=myvis, spw='30:5~7')
flagdata(vis=myvis, spw='30:56~62')
flagdata(vis=myvis, spw='30', antenna='ea02')
flagdata(vis=myvis, spw='31:2~5')
flagdata(vis=myvis, spw='31:45~47')
flagdata(vis=myvis, spw='32:36~38')
flagdata(vis=myvis, spw='2~4', scan='22')
flagdata(vis=myvis, spw='18', antenna='ea08&ea19')
flagdata(vis=myvis, spw='20', antenna='ea04&ea21')
flagdata(vis=myvis, spw='20', antenna='ea07&ea18')
flagdata(vis='myvis', antenna='ea26')      
flagdata(vis='myvis', antenna='ea08&ea24')      
flagdata(vis='myvis', antenna='ea11&ea27')      
flagdata(vis='myvis', antenna='ea15&ea17;ea18&ea27;ea06&ea19;ea08&ea17;ea17&ea19;ea02&ea15')        
flagdata(vis='myvis', antenna='ea15&ea17;ea18&ea27;ea06&ea19;ea08&ea17;ea17&ea19;ea02&ea15')     

### Defining the SPW variable:
SPW = '2~33'

### Calibration steps:
### Note that field 2 is the flux calibrator 3C286 (i.e., non-standard order of fields due to the alignment between bandpass calibration and Swift's Earth occultation.

setjy(vis=myvis, field='2', modimage='3C286_C.im', standard='Perley-Butler 2013', usescratch=False, scalebychan=True, spw='')

gaincal(vis=myvis, caltable=mylabel+'.G0all', field='2,0', refant='ea05', spw=SPW, gaintype='G', calmode='p', solint='int', minsnr=5, append=False)

gaincal(vis=myvis, caltable=mylabel+'.G0', field='2', refant='ea05', spw=SPW, calmode='p', solint='int', minsnr=5)

gaincal(vis=myvis,caltable=mylabel+'.K0', gaintable=[mylabel+'.G0'], field='2',spw=SPW,gaintype='K', refant='ea05', combine='scan', solint='inf', minsnr=3)

bandpass(vis=myvis,caltable=mylabel+'.B0', gaintable=[mylabel+'.G0',mylabel+'.K0'], field='2', spw=SPW, refant='ea05',solnorm=True, bandtype='B', combine='scan', solint='inf')

gaincal(vis=myvis, caltable=mylabel+'.G1', gaintable=[mylabel+'.K0',mylabel+'.B0'], field='2', refant='ea05', solnorm=False, spw=SPW, solint='inf', gaintype='G', calmode='ap', append=False)

gaincal(vis=myvis,caltable=mylabel+'.G1', gaintable=[mylabel+'.K0', mylabel+'.B0'], field='0', refant='ea05', solnorm=False, spw=SPW, solint='inf', gaintype='G',calmode='ap', append=True)

### Calculating the flux scale and applying the calibration tables:

myscale=fluxscale(vis=myvis, caltable=mylabel+'.G1', fluxtable=mylabel+'.fluxscale1', reference='2', transfer='0')

applycal(vis=myvis, gaintable=[mylabel+'.K0', mylabel+'.fluxscale1', mylabel+'.B0'], parang=False, field='2', gainfield=['','2',''], interp=['','nearest',''], calwt=False) 

applycal(vis=myvis, gaintable=[mylabel+'.K0', mylabel+'.fluxscale1', mylabel+'.B0'], parang=False, field='0', gainfield=['','0',''], interp=['','nearest',''], calwt=False) 

applycal(vis=myvis, gaintable=[mylabel+'.K0', mylabel+'.fluxscale1', mylabel+'.B0'], parang=False, field='1', gainfield=['','0',''], interp=['','linear',''], calwt=False) 




