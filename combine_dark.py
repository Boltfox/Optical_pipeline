import pyfits
import numpy as np 
import os

frames=[]

os.system('ls -1 *.FIT>list.txt')
file = open('list.txt', 'r')
name=file.read()
name=name.split('\n')
bias=pyfits.open('../../master_bias.fits')[0].data
for i in range(0,len(name)-2):
	im=pyfits.open(name[i])[0].data
	im=im-bias
	frames.append(im)

nor=pyfits.open(name[0])[0].header['EXPTIME']
mb=np.mean(np.dstack(frames),axis=2)
pyfits.writeto('../'+str(nor)+'dark.fits',mb)
hdu=pyfits.open('../'+str(nor)+'dark.fits')
hdu[0].header['EXPTIME']=nor
hdu.writeto('../M'+str(nor)+'dark.fits')
os.system('ls -1 *.FIT>list.txt')
hdu.close()

