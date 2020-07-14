import pyfits
import numpy as np 
import os

frames=[]

os.system('ls -1 *.FIT>list.txt') #หาไฟล์ที่ลงท้ายด้วย .FIT แล้วเขียนชื่อทั้งหมดลงใน list.txt
file = open('list.txt', 'r') #เปิดไฟล์ list.txt
name=file.read() #อ่านไฟล์
name=name.split('\n') #ปรกติเวลาเขียนไฟล์จะมี \n ซึ่งเป็นตัวขึ้่นบรรทัดใหม่ เราต้องเอาออก 
bias=pyfits.open('../../master_bias.fits')[0].data #เปิดไฟล์ชื่อ master_bias.fits
for i in range(0,len(name)-2): #อ่านชื่อไฟล์ทีละตัว
	im=pyfits.open(name[i])[0].data # แทนค่าตัวแปร im ด้วย รูปภาพ จากไฟล์ที่ i
	im=im-bias # เอารูปภาพ ลบ ด้วย ภาพไบแอส 
	frames.append(im) #

nor=pyfits.open(name[0])[0].header['EXPTIME'] #
mb=np.mean(np.dstack(frames),axis=2) #
pyfits.writeto('../'+str(nor)+'dark.fits',mb) #
hdu=pyfits.open('../'+str(nor)+'dark.fits') #
hdu[0].header['EXPTIME']=nor #
hdu.writeto('../M'+str(nor)+'dark.fits') #
os.system('ls -1 *.FIT>list.txt') #
hdu.close() #

