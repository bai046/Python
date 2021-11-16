# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:13:46 2021

@author: 瑛
"""
import pandas as pd

df4 = pd.read_csv("./dataset/green_tripdata_2014-04.csv",nrows=50)
print(df4)
print(df4.columns)
#True,False
df4.rename(columns={"Pickup_longitude":"上车经度"
                   ,"Pickup_latitude":"上车纬度"
                   ,"Dropoff_longitude":"下车经度"
                   ,"Dropoff_latitude":"下车纬度"
                   ,"Passenger_count":"乘客人数"
                   ,"Fare_amount":"费用"},inplace=False)
print(df4.columns)
'''
'''
#删除0
dataset0 = df4[(df4['Pickup_longitude']!=0) | (['Pickup_latitude']!=0) | (df4['Dropoff_longitude']!=0) | (df4['Dropoff_latitude']!=0)]
#删除空
dataset_0 = dataset0.dropna(axis=0,how="any")

dataset = df4.loc[(df4['Pickup_longitude'].astype(float) >-73.89) | (df4['Pickup_latitude'].astype(float) <40.8)| (df4['Dropoff_longitude'].astype(float) >73.9)| (df4['Dropoff_latitude'].astype(float) <40.8)
, ['Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude']]











