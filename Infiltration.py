
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


# In[102]:

df=pd.read_csv(r'C:\Users\ifue3702\Downloads\soils Ks.csv', 
               skiprows =range(0,1),
               encoding = "ISO-8859-1",
               names=['Texture', 'Ks_mm_h', 'ks_class'])
df['Ks_mm_h']
df['Ksat_mm_day']=(df['Ks_mm_h']*24)
#assuming a constant area of 1m2 at saturation
#should operate Darcy's law Q=Ks*A*Dh/Dl, but A =1, so Q=Ks*DL/Ds
#if we have a initial water column of 10 m depth
#assuming groundwater table at 10 m
text=list(df['Texture'])
a='Q_h'
text.insert(0,a)
water_depth=range(0,11)
depth_gw=10
def hydraulic_grad (water_depth, depth_gw):
    return (water_depth+10)/depth_gw
#Discharge (m3/d) at different hydraulic gradients
for i in water_depth:
    df['Q'+str(i)] = hydraulic_grad(water_depth[i], depth_gw)*df.Ksat_mm_day
df_trans=df.transpose()
df_trans.to_csv('C:\\Users\\ifue3702\\Documents\\Python Scripts\\learning\\ks_text.csv')
ot_df=pd.read_csv('C:\\Users\\ifue3702\\Documents\\Python Scripts\\learning\\ks_text.csv', 
                  skiprows=range(0,5),
                  index_col=False,
                  names=text)
graph_df=ot_df.drop('Q_h',1)
graph_df['water_depth']=graph_df.index*1000
plt.plot(graph_df['water_depth'],graph_df['Coarse Sand'])
plt.plot(graph_df['water_depth'],graph_df['Sand'])
plt.plot(graph_df['water_depth'],graph_df['Loamy Sand'])
plt.plot(graph_df['water_depth'],graph_df['Loam Fine Sandy'])
plt.plot(graph_df['water_depth'],graph_df['Sandy Loam'])
plt.plot(graph_df['water_depth'],graph_df['Fine Sandy Loam'])
plt.plot(graph_df['water_depth'],graph_df['Loam'])
plt.plot(graph_df['water_depth'],graph_df['Silt Loam'])
plt.plot(graph_df['water_depth'],graph_df['Silt'])
plt.plot(graph_df['water_depth'],graph_df['Sandy Clay Loam'])
plt.plot(graph_df['water_depth'],graph_df['Clay Loam'])
plt.plot(graph_df['water_depth'],graph_df['Silty Clay Loam'])
plt.plot(graph_df['water_depth'],graph_df['Sandy Clay'])
plt.plot(graph_df['water_depth'],graph_df['Silty Clay'])
plt.plot(graph_df['water_depth'],graph_df['Clay'])

#graph_df.plot(graph_df['water_depth'],graph_df['Coarse Sand'])
plt.xlabel('Water Depth (mm)')
plt.ylabel('Infiltration rate (mm/d)')
plt.grid(which='both')
plt.show()

#http://www.fao.org/docrep/s8684e/s8684e0a.htm
#http://pubs.usgs.gov/wsp/1544f/report.pdf


# In[16]:

help(pd.read_csv)

