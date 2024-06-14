# X-ray spectral analysis

Both the light curve and spectral analysis are based on the data products from the online Swift XRT pipeline, as described in the main paper.

Note that the light curve analysis, based on the Swift pipeline, is fully performed in the NOTEBOOKS/Lightcurves.ipnyb Jupyter Notebook. 

To reproduce the X-ray spectral analysis, open XSpec in a terminal in this folder.
(see https://heasarc.gsfc.nasa.gov/xanadu/xspec/ for the XSpec software)

In xspec, run the command

@fitting_and_flux.tcl

That will reproduce the entire analysis and produce a plot of the fit as well. 

## The main output to pay attention to are, in X-spec format:

### 1) the fitted parameters:

========================================================================

Model TBabs<1>(bbody<2> + powerlaw<3>) Source No.: 1   Active/On

Model Model Component  Parameter  Unit     Value

 par  comp

   1    1   TBabs      nH         10^22    6.83141      +/-  0.358629     

   2    2   bbody      kT         keV      1.84437      +/-  4.01336E-02  

   3    2   bbody      norm                2.68085E-02  +/-  6.29378E-04  

   4    3   powerlaw   PhoIndex            3.70567      +/-  0.283101   
  
   5    3   powerlaw   norm                2.14402      +/-  0.678852   
  
________________________________________________________________________


Fit statistic  : Chi-Squared                  956.83     using 889 bins.

Test statistic : Chi-Squared                  956.83     using 889 bins.
 Null hypothesis probability of 4.43e-02 with 884 degrees of freedom

 Parameter   Confidence Range (1)

     1      6.47716      7.18731    (-0.354255,0.3559)

     2      1.80883      1.88246    (-0.0355439,0.0380872)

     3    0.0261473     0.027384    (-0.000661159,0.000575506)

     4      3.43401      3.96734    (-0.271654,0.261666)

     5      1.57578       2.9007    (-0.568242,0.756682)

### 2) the fitted flux:

========================================================================

Model TBabs<1>*cflux<2>(bbody<3> + powerlaw<4>) Source No.: 1   Active/On

Model Model Component  Parameter  Unit     Value

 par  comp

   2    2   cflux      Emin       keV      0.500000     frozen

   3    2   cflux      Emax       keV      10.0000      frozen

   4    2   cflux      lg10Flux   cgs      -8.07877     +/-  0.121742    
 
________________________________________________________________________

 Parameter   Confidence Range (1)

     4      -8.1909     -7.95675    (-0.112133,0.122022)

