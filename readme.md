# **Marine Gravity Tools**
A program package(**T**ools) to processing **M**arine **G**ravity data, which is a multi-langulage package,such as **C++**, **Python**, **Fortran** and **Batch** or **Powershell** script to run program.


# C++

# Python

# Fortran

# Batch and Powershell

```python
# -*- coding: utf-8 -*-
""" 
--------Airy���ⲹ��ģ��ʾ��ͼ��P183 fig5.6
--------��־ظ��2016/7/19������
--------�ο����ף�A. B. Watts��2001
--------------------�޸�˵��------------------------------------
 
----------------------------------------------------------------

"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
# from matplotlib.font_manager import FontProperties
from os import path
from matplotlib.ticker import  MultipleLocator
from matplotlib.ticker import  FormatStrFormatter
from matplotlib.patches import Polygon

import RWData.SaveDat as SDat
#�����ֵ�����
#	print path.abspath(matplotlib.matplotlib_fname())	#��ǰʹ�õ������ļ�
matplotlib.rcParams["figure.autolayout"]="TRUE"	#ͼƬ�߾�
matplotlib.rcParams["font.family"]="Times New Roman"
matplotlib.rcParams["text.color"]="black"
matplotlib.rcParams["axes.linewidth"]="2"				#�������߿�
matplotlib.rcParams["font.size"]="16"
matplotlib.rcParams["xtick.major.size"]=10				#xtick����
matplotlib.rcParams["xtick.minor.size"]=5
matplotlib.rcParams["xtick.major.width"]=2
matplotlib.rcParams["xtick.minor.width"]=1
matplotlib.rcParams["ytick.major.size"]=10				#ytick����
matplotlib.rcParams["ytick.minor.size"]=5
matplotlib.rcParams["ytick.major.width"]=2
matplotlib.rcParams["ytick.minor.width"]=1
matplotlib.rcParams["lines.linewidth"]=4				#��������
matplotlib.rcParams["mathtext.default"]="regular"		#��ʽ����:tt, it, rm, cal, sf, bf or default/regular (non-math)
#------------------------������ʽ��ͼ----------------------------
#1. ͼƬ�������ã���С�������
plt.figure(figsize=(9,5))
ymin=-2
ymax=1
xmin=1.2
xmax=6.8
size_text=18
x = np.linspace(xmin, xmax, 100)
y1 = np.sin(x)*0.5
y2=-np.sin(x)*0.4-1.3
with plt.xkcd():
	plt.fill_between(x, y2,y1, facecolor='grey', interpolate=True, alpha=0.3)
	plt.axhline(0,ls="--",color=(0,0,0))
	y_sealevel=ymax*0.8
	plt.axhline(y_sealevel,color='b',alpha=0.5)
	plt.text(6,y_sealevel,"Sea-level",va="bottom",size=size_text)
	plt.text(4.5,0.3,"Water\n$\\rho_{w}$",ha="center",va="center",size=size_text)
	plt.text(2.5,0.4,"h(x)",ha="center",va="center",rotation="-20",size=size_text)
	plt.text(2,-0.9,"Oceanic Crust\n$\\rho_{c}$",ha="center",va="center",bbox=dict(boxstyle="Round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),alpha=0.5),size=size_text)
	#��������
	verts = [(xmin, y_sealevel)] + list(zip(x, y1)) + [(xmax, y_sealevel)]
	poly = Polygon(verts, facecolor='lightblue', edgecolor='0.5')
	plt.gca().add_patch(poly)
	#plt.arrow(6,y_sealevel,0,-y_sealevel, head_width=0.05, head_length=0.1, fc='k', ec='k',shape="full",length_includes_head=True,dict(arrowstyle="->"))
	plt.annotate('', xy=(6,y_sealevel), xytext=(6,0),arrowprops=dict(arrowstyle="<->"))
	plt.text(5.9,0.5,"d",ha="right",va="center",size=size_text)
	#����������ָʾ��ͷ
	plt.annotate('', xy=(2,0.9),
					  xytext=(1,0.3),
					  arrowprops=dict(arrowstyle="<->",
									  
									  ec="k",
									  connectionstyle="angle,angleA=90,angleB=0,rad=10"
									  )
					  )
	plt.text(1.5,0.9,"x",ha="right",va="bottom",size=size_text)
	plt.text(1.05,0.5,"y",ha="left",va="center",size=size_text)
	#���ⲹ����
	plt.fill_between(x, ymin,y2, facecolor=(237/255.0,28/255.0,36/255.0),interpolate=True)
	y_t=-1.3
	plt.axhline(y_t,ls="--",color=(0,0,0))
	plt.text(4.5,-1.7,"Mantle\n$\\rho_{m}$",ha="center",va="center",size=size_text)
	plt.text(2.5,-1.65,"r(x)",ha="center",va="center",rotation="15",size=size_text)
	plt.annotate('', xy=(6,0), xytext=(6,y_t),arrowprops=dict(arrowstyle="<->"))
	plt.text(5.9,-0.8,"t",ha="right",va="center",size=size_text)
plt.ylim(ymin,ymax)
plt.xlim(1,7)
plt.subplots_adjust(left=0)
plt.subplots_adjust(bottom=0.1)
plt.axis('off')
#����
plt.show()
# plt.savefig(u"pdf\\Airy���ⲹ��ģ��ʾ��ͼ.pdf")
# plt.savefig(u"png\\Airy���ⲹ��ģ��ʾ��ͼ.png",dpi=300)





```