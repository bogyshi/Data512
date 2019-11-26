import os
import sys
import pandas as pd
import numpy as np
import datetime

def createHouseToTypeMappings():
    colsOfInterest=['LCLid','stdorToU','Acorn','Acorn_grouped']
    d = '../data/Power-Networks-LCL-June2015(withAcornGps).csv_Pieces/'
    dp = ''
    dfs = []
    counter = 1
    for filename in os.listdir(d):
        inFile = pd.read_csv(os.path.join(d,'Power-Networks-LCL-June2015(withAcornGps)v2_'+str(counter)+'.csv'),header=0,usecols=colsOfInterest)
        dfs.append((inFile.groupby(colsOfInterest).size().reset_index().rename(columns={0:'count'})))
        counter+=1

    pd.concat(dfs).groupby(colsOfInterest).sum().to_csv('../data/houseData.csv')

def sepAllData():
    colsOfInterest=['LCLid', 'DateTime', 'KWH/hh (per half hour) ']
    counter = 1
    d = '../data/Power-Networks-LCL-June2015(withAcornGps).csv_Pieces/'
    od = '../data/pivotData/'
    for filename in os.listdir(d):
        if(os.path.isfile(os.path.join(od,'block'+str(counter)+'sep.csv'))):
            print('already did file' + str(counter))
            pass
        else:
            try:
                inFile = pd.read_csv(os.path.join(d,'Power-Networks-LCL-June2015(withAcornGps)v2_'+str(counter)+'.csv'),header=0,usecols=colsOfInterest)
                inFile.columns = ['LCLid', 'DateTime', 'KWH/hh']
                inFile['DateTime'] = pd.to_datetime(inFile.DateTime,format='%Y-%m-%d %H:%M:%S')
                inFile = inFile.iloc[((inFile.DateTime >= '2013-01-01').values & (inFile.DateTime < '2014-01-01')).values]
                inFile['KWH/hh'] = inFile['KWH/hh'].astype(float)
                inFile['Date'] = [datetime.datetime.date(d) for d in inFile['DateTime']]
                inFile['Time'] = [datetime.datetime.time(d) for d in inFile['DateTime']]
                inFile.pivot_table(values='KWH/hh',index=['LCLid','Date'],columns='Time').to_csv(os.path.join(od,'block'+str(counter)+'sep.csv'))
            except:
                print('had a null in block: ' + str(counter))
                inFile = pd.read_csv(os.path.join(d,'Power-Networks-LCL-June2015(withAcornGps)v2_'+str(counter)+'.csv'),header=0,usecols=colsOfInterest)
                inFile.columns = ['LCLid', 'DateTime', 'KWH/hh']
                inFile['DateTime'] = pd.to_datetime(inFile.DateTime,format='%Y-%m-%d %H:%M:%S')
                inFile = inFile.iloc[((inFile.DateTime >= '2013-01-01').values & (inFile.DateTime < '2014-01-01') & (inFile['KWH/hh']!='Null')).values]
                inFile['KWH/hh'] = inFile['KWH/hh'].astype(float)
                inFile['Date'] = [datetime.datetime.date(d) for d in inFile['DateTime']]
                inFile['Time'] = [datetime.datetime.time(d) for d in inFile['DateTime']]
                inFile.pivot_table(values='KWH/hh',index=['LCLid','Date'],columns='Time').to_csv(os.path.join(od,'block'+str(counter)+'sep.csv'))
        counter+=1

def handleSpills():
    counter = 1
    od = '../data/pivotData/'
    pairWiseCommon1=np.array([])
    pairWiseCommon2=np.array([])
    overlappingHouses=[]
    for filename in os.listdir(od):
        vals = pd.read_csv(
            os.path.join(od,'block'+str(counter)+'sep.csv'),header=0)
        totvals+=len(vals)
        if(counter<2):
            pairWiseCommon1 = np.unique(vals['LCLid'])
        else:
            pairWiseCommon2=np.unique(vals['LCLid'])
            pw = np.intersect1d(pairWiseCommon1,pairWiseCommon2)
            if(len(pw)>0):
                prevDF = pd.read_csv(os.path.join(od,'block'+str(counter)+'sep.csv'),header=0)
                prevOverlap = prevDF.iloc[prevDF['LCLid'].isin(pw).values]
                thisOverlap = vals.iloc[vals['LCLid'].isin(pw).values]
                overlappingHouses.append(prevOverlap)
                overlappingHouses.append(thisOverlap)
                vals.iloc[~vals['LCLid'].isin(pw).values].to_csv(os.path.join(od,'block'+str(counter)+'sep.csv'))
                prevDF.iloc[~prevDF['LCLid'].isin(pw).values].to_csv(os.path.join(od,'block'+str(counter-1)+'sep.csv'))

            pairWiseCommon1 = pairWiseCommon2
        counter+=1
'''
Order should be sepAllData then handleSpills
'''

'''
t = pd.read_csv('../data/houseData.csv',header=0)
t[t.]
np.unique(pd.read_csv('../data/houseData.csv',header=0)['LCLid']).shape


d = '../data/Power-Networks-LCL-June2015(withAcornGps).csv_Pieces/'

t = pd.read_csv(os.path.join(d,'Power-Networks-LCL-June2015(withAcornGps)v2_'+str(1)+'.csv'),header=0)

'''
