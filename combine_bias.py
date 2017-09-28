import pyfits
import numpy as np 
import os

frames=[]

os.system('ls -1 *.FIT>list.txt')
file = open('list.txt', 'r')
name=file.read()
name=name.split('\n')
for i in range(0,len(name)-2):
	#nor=pyfits.open(name[i])[0].header['EXPTIME']
	im=pyfits.open(name[i])[0].data
	im=im
	frames.append(im)

mb=np.mean(np.dstack(frames),axis=2)

pyfits.writeto('../master_bias.fits',mb)

