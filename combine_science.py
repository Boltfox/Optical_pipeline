import pyfits
import numpy as np 
import os

bframes=[]
#vframes=[]
rframes=[]

os.system('ls -1 *.FIT>list.txt')
file = open('list.txt', 'r')
name=file.read()
name=name.split('\n')
bias=pyfits.open('../master_bias.fits')[0].data
#dark=pyfits.open('../master_dark.fits')[0].data
bflat=pyfits.open('../Blueflat.fits')[0].data
rflat=pyfits.open('../Resflat.fits')[0].data
bdark=pyfits.open('../Bluedark.fits')[0].data
rdark=pyfits.open('../Resdark.fits')[0].data
for i in range(0,len(name)-2):
	hdu=pyfits.open(name[i])
	nor=hdu[0].header['EXPTIME']
	fil=hdu[0].header['FILTER']
	if (fil=='Blue (B)'):
		#im=im/np.mean(im)
		im=(hdu[0].data-bias-bdark)
		im=im/(bflat)
		pyfits.writeto('B'+name[i],im)
		print name[i]
	if (fil=='Red (B)'):
		im=(hdu[0].data-bias-rdark)
		im=im/(rflat)
		pyfits.writeto('R'+name[i],im)
		print name[i]
	hdu.close()
os.system('ls -1 R*.FIT>listRB.txt')
os.system('ls -1 B*.FIT>>listRB.txt')
file5 = open('listRB.txt', 'r')
name2=file5.read()
name2=name2.split('\n')
for i in range(0,len(name2)-2):
	heu=pyfits.open(name2[i])
	heu[0].header['EXPTIME']=nor
	heu[0].header['FILTER']=fil
	heu.writeto('H'+name2[i])
	

#rmb=np.mean(np.dstack(bframes),axis=2)


