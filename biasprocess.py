import pyfits
import numpy as np 
name1=
name2=
name3=
bias1=pyfits.open(name1)[0].data
print bias1
print bias1/100
bias2=pyfits.open(name2)[0].data
print bias1/bias2
d=bias1/bias2
frames=[]
frames.append(bias1)
frames.append(bias2)
bias3=pyfits.open(name3)[0].data
frames.append(bias3)
mb=np.mean(np.dstack(frames),axis=2)
hdu.writeto(out)
#import sys 

