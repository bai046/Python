# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:21:34 2021

@author: 瑛
"""



def Read_Write_File(filePath,mode_Type,Ope_Choice,size = None):
    '''
    filePath:   为文件路径+文件名 例如：D:\Python\Foundation Stage\stage1\text.text
    mode_Type:  r|w|a
    size:       读取内容的大小，默认为None，整型
    Ope_Choice: 读写操作read|write
    '''
    if Ope_Choice == "read":
        f = open("filePath","mode_Type","Ope_Choice",encoding="utf-8")
        print(f.read(size))
        f.close()
    elif Ope_Choice == "write":
        f = open("filePath","mode_Type","Ope_Choice",encoding="utf-8")
        print(f.write("write写了这个文件"))
        f.close()
    else:
        print("请填写操作类型（read|write）")

    

    









