#!/usr/bin/env python
# coding: utf-8

# In[9]:

#IMPORT DELLE LIBRERIE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import sys
import os

# In[10]:
if not os.path.exists("images"):
    os.mkdir("images")

#IMPORT DEI DATI
if len(sys.argv) < 6:
     sys.exit("Wrong Usage, use : python plot_try.py [Path] [Capacity] [IsDirect] [TitoloRtt] [TitotoCapacita]")

path = sys.argv[1]
Cap = int(sys.argv[2])
IsDirect = int(sys.argv[3])
TitoloRtt= sys.argv[4]
TitoloCap= sys.argv[5]

data= pd.read_csv(path,delimiter=' ')
data
# In[11]:

#Definizioni per RTT

maxSize = 1472 #Max Size deriva da 1500=MTU - 20 byte IPHeader - 8byte ICMPHeader
L2size  = 1538 #total size with max payload =1500
headers = 58  #ICMP + IP + Ethernet

def getLenght(s):
    mod = (s%maxSize)
    a = (s // maxSize) * L2size
    if (mod != 0):
        a = a + mod + getPadding(mod) + headers
    return a

def getPadding(x):
    if (x < 18): return 18-x
    return 0

def getRttTheory(d, C):
    return 2*d*8*(10**3)/(C)

def getRttTheory_Switch(d, C):
    if(d<=1538):
        return 2*getRttTheory(d,C)
    return getRttTheory(d,C) + getRttTheory(1538,C) 
    
getLenght  = np.vectorize(getLenght)
getPadding = np.vectorize(getPadding)
getRttTheory_Switch= np.vectorize(getRttTheory_Switch)
# In[12]:

#Calcolo effettivo dei valori

Size = data['Size'].to_numpy()

RttMin = data['RttMin'].to_numpy()
RttAvg = data['RttAvg'].to_numpy()
RttMax = data['RttMax'].to_numpy()

lenght = getLenght(Size)

if(IsDirect==1):
    RttTheory = getRttTheory(lenght, Cap)
else :
    RttTheory = getRttTheory_Switch(lenght, Cap)
# In[13]:

#Stampa RTT
fig = px.line(x=lenght, y= [RttMin, RttAvg, RttMax, RttTheory],
            markers=True ,labels=dict(x="Data [bytes]", value="RTT [ms]", variable="Tipologia di RTT"),
            width=800, height= 600)

if(IsDirect==1):
    newnamesFig = {'wide_variable_0':'RttMin', 'wide_variable_1':'RttAvg', 'wide_variable_2':'RttMax', 'wide_variable_3': 'RttTheory'}
else :
    newnamesFig = {'wide_variable_0':'RttMin', 'wide_variable_1':'RttAvg', 'wide_variable_2':'RttMax', 'wide_variable_3': 'RttTheorySwitch'}

fig.for_each_trace(lambda t: t.update(name = newnamesFig[t.name],
                                      legendgroup = newnamesFig[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnamesFig[t.name])
                                     )
                  )
fig.update_layout(
    legend=dict( yanchor="top", y=0.90, xanchor="left",x=0.01),
    title={'text': TitoloRtt, 'x':0.5, 'xanchor': 'center','yanchor': 'top'}
)
fig.show()
fig.write_image("images/"+TitoloRtt+".pdf")
# In[14]:

#Definizioni per la capacità
def getCapacity_sec(d, rtt):
    x=  2*8*d/rtt/1000
    return x

# 2.4 nel caso di 10Mbit/s, altrimenti 0.24 per 100Mbit/s
if(Cap== (10*10**6)):
    RttMTUfisso= 2.4
else: #do per scontato sia 100*10**6, quindi 100Mbit/s
    RttMTUfisso= 0.24

def getCapacity_sec_TheorySwitch(d, rtt):
    if(d<=1538):
        return 2*getCapacity_sec(d, rtt)
    return 2*8*d/(rtt - RttMTUfisso)/1000

getCapacity_sec_TheorySwitch= np.vectorize(getCapacity_sec_TheorySwitch)
# In[15]:

#Calcolo delle capacità
if(IsDirect==1):
    Speed= getCapacity_sec(lenght, RttMin)
    SpeedTheory = getCapacity_sec(lenght, RttTheory)
else :
    Speed= getCapacity_sec_TheorySwitch(lenght, RttMin)
    SpeedTheory = getCapacity_sec_TheorySwitch(lenght, RttTheory)
# In[16]:

#STAMPA CAPACITA'

fig2 = px.line(x=lenght,y= [Speed, SpeedTheory],
            labels=dict(x="Data [bytes]", value="Capacity [Mbit/s]", variable="Types of Capacity"),
            width=800, height= 600)

if(IsDirect==1):
    newnamesFig2 = {'wide_variable_0':'Capacity(RTTmin)', 'wide_variable_1':'Capacity(RttTheory)'}
else:
    newnamesFig2 = {'wide_variable_0':'Capacity(RTTmin)', 'wide_variable_1':'Capacity(RttTheorySwitch)'}

fig2.for_each_trace(lambda t: t.update(name = newnamesFig2[t.name],
                                      legendgroup = newnamesFig2[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnamesFig2[t.name])
                                     )
                  )

fig2.update_layout(
    legend=dict( yanchor="top", y=0.90, xanchor="left",x=0.01),
    title={'text': TitoloCap, 'x':0.5, 'xanchor': 'center','yanchor': 'top'}
)
fig2.show()
fig2.write_image("images/"+TitoloCap+".pdf")