# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:21:55 2021

@author: 瑛
"""
#	1 2 3	迭代
for x in (1, 2, 3): print (x,)

#字典
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
key = dict.keys()
item = dict.items()
print(key)
print(item)

for key,value in dict.items():
    print(key,value)
    

#集合set
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
#enumerate()返回两个值（值+值的索引）
for i,j in enumerate(thisset):
    print(i,j)
    





























