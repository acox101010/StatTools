import streamlit as st
import numpy as np
import os, sys
import matplotlib.pyplot as plt
import pandas as pd
import tables
from glob import glob

#Read and cleanup excel file
st.title('Application for Plotting Positive Pressure Data (STP-0120)')
st.sidebar.title('Graph manipulation tools')
path = st.text_input('.xlsx file path')

if path:
    file_direct = path
allfiles = []
for file in os.listdir(file_direct):
    if file.endswith('.XLSX') or file.endswith('.XLS'):
        allfiles.append(file)
if st.checkbox('Display data files in directory'):
    st.subheader('data files')
    st.write(allfiles)

n = st.sidebar.number_input('File #:',0,100,1) #variable for list entry
end_val = st.sidebar.slider('End Value',-10000,-10,-10) #variable for removing last breath

#clean data
new_path = path + "\\" + str(allfiles[n])
df = pd.read_excel(new_path) #reading datafile
df = df.drop([0,1,2,3,4,5,6,7,8,9,10,11,12,13],axis=0) #drop first 15 rows
df.rename(columns = {'05947':'Time stamp','Unnamed: 2':'Time(sec)','Unnamed: 3':'In H20'}, inplace = True) 

if st.checkbox('Display data for file'):
    st.subheader('processed data')
    st.dataframe(df)
    
#plot all data
st.subheader("All run data")
ydat = df['In H20']
xdat = df['Time(sec)']
fig,ax = plt.subplots(figsize=(10,7))
ax.plot(xdat[0:end_val],ydat[0:end_val],lw = .8, color='C0')
ax.set_title(('Raw File Name: '+allfiles[n]),alpha = .7, size=12)
ax.set_xlabel('Elapsed Time (seconds)')
ax.set_ylabel('Mask Pressure (in. w.c.)')
plt.axhline(y=0,xmin=0, xmax=2000, ls='--', color='r' )
plt.axhline(y=3.5,xmin=0, xmax=2000, ls='--', color='r' )
st.pyplot(fig)
st.subheader("All run stats")
st.write("Maximum:",ydat[0:end_val].max(),"Minimum:", ydat[0:end_val].min(),
                "Mean:", ydat[0:end_val].mean())

#plot primary data
st.subheader("Primary data")
p_end_val = st.sidebar.slider('Primary End Value',1,300000,10000) #variable for stopping last breath
fig,ax = plt.subplots(figsize=(10,7))
ax.plot(xdat[0:p_end_val],ydat[0:p_end_val],lw = .8, color='C0')
ax.set_title(('Raw File Name: '+allfiles[n]),alpha = .7, size=12)
ax.set_xlabel('Elapsed Time (seconds)')
ax.set_ylabel('Mask Pressure (in. w.c.)')
plt.axhline(y=0,xmin=0, xmax=2000, ls='--', color='r' )
plt.axhline(y=3.5,xmin=0, xmax=2000, ls='--', color='r' )
st.pyplot(fig)
st.subheader("Primary run stats")
st.write("Maximum:",ydat[0:p_end_val].max(),"Minimum:", ydat[0:p_end_val].min(),
                "Mean:", ydat[0:p_end_val].mean())

waves = st.sidebar.radio("Waveform Zoom", ("False", "True"))
if waves == "True":
    st.sidebar.subheader("select data range")
    B = st.sidebar.number_input("begin value", 1, 500000, step = 100)
    E = st.sidebar.number_input("end value", 1, 500000, step = 100)
    #plot waveform selection
    st.subheader("variable data plot")
    fig,ax = plt.subplots(figsize=(10,7))
    ax.plot(xdat[B:E],ydat[B:E],lw = .8, color='C0')
    ax.set_title(('Zoomed data: '+allfiles[n]),alpha = .7, size=12)
    ax.set_xlabel('Elapsed Time (seconds)')
    ax.set_ylabel('Mask Pressure (in. w.c.)')
    plt.axhline(y=0,xmin=0, xmax=2000, ls='--', color='r' )
    plt.axhline(y=3.5,xmin=0, xmax=2000, ls='--', color='r' )
    st.pyplot(fig)
    


