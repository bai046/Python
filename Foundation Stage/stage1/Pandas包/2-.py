# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 08:13:38 2021

@author: 瑛
"./dataset/green_tripdata_2014-04.csv"
"./dataset/green_tripdata_2014-05.csv"
"""
import pandas as pd
#import numpy as np
df = pd.read_csv("./dataset/green_tripdata_2014-04.csv", header=0, encoding='utf-8', dtype=str)
df2 = pd.read_csv("./dataset/green_tripdata_2014-05.csv", header=0, encoding='utf-8', dtype=str)
#print(df.columns)
df.rename(columns={"Pickup_longitude":"上车经度"
                   ,"Pickup_latitude":"上车纬度"
                   ,"Dropoff_longitude":"下车经度"
                   ,"Dropoff_latitude":"下车纬度"
                   ,"Passenger_count":"乘客人数"
                   ,"Fare_amount":"费用"},inplace=True)
df2.rename(columns={"Pickup_longitude":"上车经度"
                   ,"Pickup_latitude":"上车纬度"
                   ,"Dropoff_longitude":"下车经度"
                   ,"Dropoff_latitude":"下车纬度"
                   ,"Passenger_count":"乘客人数"
                   ,"Fare_amount":"费用"},inplace=True)
print(df.columns)

ddf = df[df[:]!=0]
print(ddf)

#使用“或”条件进行筛选
dataset = ddf.loc[(ddf['上车经度'] >-73.89) | (ddf['上车纬度'] <40.8)| (ddf['下车经度'] >73.9)| (ddf['下车纬度'] <40.8)
, ['上车经度','上车纬度','下车经度','下车纬度']]
print(dataset)

import os
path = './dataset/'
files = os.listdir(path)
train_csv = list(filter(lambda x:(x[0:6] == 'train_' and x[-4:] == '.csv'),files))
data_list = []
for fileitem in train_csv:
    tmp = pd.read_csv(path + fileitem,header=0)
    data_list.append(tmp)
dataset = pd.concat(data_list,ignore_index = False)