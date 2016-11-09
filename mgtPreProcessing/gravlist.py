# -*- coding: utf-8 -*-
import linecache
import time
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons

#according to the manual document of the Lacost gravity define dict 
col_name={'datetime':1,'day':2,'grav':3,'spring':4,'beam':5,'vcc':6,'al':7,'ax':8,'ve':9,'ax2':10,'xacc2':11,'lacc2':12,'crossaccel':13,'longaccel':14,'etovos':15,'lon':16,'lat':17,'velocity':18,'heading':19,'1':1}
# get perticular column of the recode of the gravity survey
def getcol(filename,colVec):
    AllData = linecache.getlines(filename)
    rows=len(AllData)
    cols=len(colVec)
    col_index=[]
    for i in range(0,cols):
        col_index.append(col_name.get(colVec[i]))
    coldata=np.linspace(0,1.0,rows).reshape(-1,1)+np.arange(0,cols)
    for i in range(0,rows):
        linedata=AllData[i].split(',',1)[1].split(',')
        linearray=np.asarray(linedata)
        linearray=linearray[0:len(linearray)-1]
        for j in range(0,cols):
            if(col_index[j]==1):
                str_date=linearray[0].replace(' ','')
                linearray[1]=linearray[1].replace(' ','')
                str_time=linearray[1].split('.')[0]
                datetime0=time.strptime(str_date+' '+str_time,"%Y/%m/%d %H:%M:%S")
                timeStamp = int(time.mktime(datetime0)) #transform to integer
                # time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timeStamp)) #invert transform
                coldata[i][j]=timeStamp
            else:
                coldata[i][j]=linearray[col_index[j]]
    linecache.clearcache()
    return coldata


def plot_g_v_p_h(data,colname):
    import matplotlib
    import matplotlib.pyplot as plt
    import PlotImage.setting as PltSetting
    print 'plot by python' 
    # //////////////////////////////////////////
    imagewith=7					#图像宽度：cm
    imageheight=7				#图像高度：cm
    Font_title_size=24			#图像标题文字大小：p
    PltSetting.main()
    fig=plt.figure(figsize=(imagewith,imageheight))
    rows=len(colname)-1
    for i in range (0,rows):
        fig1=fig.add_subplot(rows,1,i+1)
        p,=fig1.plot(data[::,0],data[::,i+1])
        fig1.set_xlabel('longitude(degree)')
        fig1.set_ylabel(colname[i+1])
    plt.show()
	


