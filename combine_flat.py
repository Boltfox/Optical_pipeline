import pyfits
import numpy as np 
import os

bframes=[]
#vframes=[]
rframes=[]

os.system('ls -1 *FLAT*.FIT>list.txt')
file = open('list.txt', 'r')
name=file.read()
name=name.split('\n')
bias=pyfits.open('../../master_bias.fits')[0].data
Rdark=pyfits.open('../../Resdark.fits')[0].data
Bdark=pyfits.open('../../Bluedark.fits')[0].data


for i in range(0,len(name)-2):
	nor=pyfits.open(name[i])[0].header['EXPTIME']
	fil=pyfits.open(name[i])[0].header['FILTER']
	if (fil=='Blue (B)'):
		im=(pyfits.open(name[i])[0].data-bias-Bdark)
		im=im/np.mean(im)
		bframes.append(im)
	if (fil=='Red (B)'):
		im=(pyfits.open(name[i])[0].data-bias-Rdark)
		im=im/np.mean(im)
		rframes.append(im)

bmb=np.mean(np.dstack(bframes),axis=2)
pyfits.writeto('../../'+'Blue'+'flat.fits',bmb)
rmb=np.mean(np.dstack(bframes),axis=2)
pyfits.writeto('../../'+'Res'+'flat.fits',rmb)

