# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:34:15 2021

@author: 瑛
"""
#==============================================================================
# 1.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#==============================================================================
# 输入一个5位数，判断它是否是回文数：
a = int(input(" 请输入一个5位整数："))
s = str(a)
if s[0] == s[-1] and s[1] == s[-2]:
    print(" %d 是一个回文数！" % a)
else:
    print(" %d 不是一个回文数！" % a)
    
#==============================================================================
# 2.有一个已经排好序的数组ln=[1,2,3,4,5,11]，先输入一个数，请按原来的规律将它插入数组中.
#首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
#参考：https://www.runoob.com/python/python-exercise-example39.html
#==============================================================================
n = int(input(" 请输入一个数："))
list = [1,2,3,4,5,11]
list.append(n)
print(list)
for i in range (len(list)-2,0,-1):
    if list[i]>list[i+1]:
        list[i],list[i+1]=list[i+1],list[i]
print(list)


#==============================================================================
# 3.字典增删操作：毕业联系方式管理系统
#参考：https://blog.csdn.net/Artificial_idiots/article/details/111792966
#==============================================================================
info_list = []  # 用来存放所有学生数据，每一个学生的数据都是一个列表
while True:
    # 1、界面
    print("---------------------------------------------------------------")
    print("毕业联系方式管理系统")
    print("[1]增加学员信息")
    print("[2]删除学员信息")
    print("[3]退出系统")
    print("---------------------------------------------------------------")
    # 2、输入，接收用户的输入的数字，执行对应的操作
    command = int(input("请输入1到3之间的数字，进行对应操作："))
    # 3、通过判断用户输入的数字是1，还是2，还是3执行对应的操作
    if command == 1:
        # 添加学生信息
        # 让用户输入姓名、年龄、电话
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        mobile = input("请输入电话：")
        # [name, age, mobile]
        info_list.append({"name": name, "age": age, "mobile": mobile})
        print(info_list)

    elif command == 2:
        # 删除学生信息
        name = input("请输入姓名：")
        # 遍历info_list这个列表(要找到这个人)
        for i in info_list:
            if name in i.values():
                # 在这个列表中就执行删除#
                info_list.remove(i)
                print("删除成功！")
                break  # 已经找到这个人了，后面的人就不需要在遍历
        else:
            print("查无此人！")
        print(info_list)

    elif command == 3:
        # 退出系统
        print("退出成功！谢谢使用！")
        break













