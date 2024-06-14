query yes

@bbody_po.xcm

fit

error 1. 1-5

cpd /xs
setplot ene
setplot reb 3 10
pl ufspec ld rat res


editmod tbabs*cflux*(bbody+po)
0.5
10
-8

freeze 6
fit
error 1. 4