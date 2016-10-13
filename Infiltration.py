
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
#converting ks from hours to day
df['Ksat_mm_day']=(df['Ks_mm_h']*24)

'''assuming a constant area of 1m2 at saturation
should operate Darcy's law Q=Ks*A*Dh/Dl, but A =1, so Q=Ks*DL/Ds
if we have a initial water column of 10 m depth
assuming groundwater table at 10 m'''

#creating list of textures to use after and adding a data in it
text=list(df['Texture'])
a='Q_h'
text.insert(0,a)
#the depth of the ponded water from 0 to 10 m
water_depth=range(0,11)
#water table is defined at 10 m below surface
depth_gw=10
#create function of hydraulic gradient to use in Darcy's equation
def hydraulic_grad (water_depth, depth_gw):
    return (water_depth+10)/depth_gw

#add columns with different discharge rates (m3/d) at different hydraulic gradients using darcy's formulae
for i in water_depth:
    df['Q'+str(i)] = hydraulic_grad(water_depth[i], depth_gw)*df.Ksat_mm_day
#transpose df to work in it
df_trans=df.transpose()
#save df as csv
df_trans.to_csv('C:\\Users\\ifue3702\\Documents\\Python Scripts\\learning\\ks_text.csv')
#open the new csv transposed
ot_df=pd.read_csv('C:\\Users\\ifue3702\\Documents\\Python Scripts\\learning\\ks_text.csv',
                  skiprows=range(0,5),
                  index_col=False,
                  names=text)
#remove unwanted column
graph_df=ot_df.drop('Q_h',1)
#transform water depth from m to mm
graph_df['water_depth']=graph_df.index*1000
#add new column with mean daily evaporation (mm/d)
graph_df['Mean_evap']=5.725221
#remove non text data from text
text.remove('Q_h')
#add new colums with daily water losses = ET+infiltration (mm/d)
for i in text:
    graph_df[str(i)+'_losses']=graph_df[i]+graph_df.Mean_evap


#plotting Infiltration against water depth of all the soils in one graph
for i in text:
    plt.plot(graph_df['water_depth'],graph_df[i])

#unnecesary (improved code with loop)
'''plt.plot(graph_df['water_depth'],graph_df['Coarse Sand'])
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
plt.plot(graph_df['water_depth'],graph_df['Clay'])'''

#plot settings
plt.xlabel('Water Depth (mm)')
plt.ylabel('Infiltration rate (mm/d)')
plt.grid(which='both')



#to see the plot unhash the next line
#plt.show()

#to see DataFrame
print(graph_df)

#others Ks data for textures
#http://www.fao.org/docrep/s8684e/s8684e0a.htm
#http://pubs.usgs.gov/wsp/1544f/report.pdf
