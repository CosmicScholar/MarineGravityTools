# -*- coding: utf-8 -*-
import os
import time
import types
import mgtPreProcessing.gravlist as gravlist
import RWData.SaveDat as sdat
os.system('cls')

# ======input par=======
inputpath='G:\\Data\\4-SWIR-Gravity-bathy\\DY115-20-VII\\Profiles\\'
outputpath='G:\\Data\\4-SWIR-Gravity-bathy\\DY115-20-VII\\0-Preprocessing\\'
filename='2009_031.S-129'
extname='.DAT'
colname=['lon','lat','grav','velocity','heading','datetime']
plotYN=1        #if plot the data set 1; otherwise set 0
# list the data===================================================
gravfile=inputpath+filename+extname
data=gravlist.getcol(gravfile,colname)

# ========save data to file===========
sdat.SaveMat(outputpath+filename+'.dat',data,colname)
gravlist.plot_g_v_p_h(data,colname)
# print data[::,0]
