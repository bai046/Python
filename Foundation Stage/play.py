# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:50:08 2021

@author: 瑛
"""
info_list = []  # 用来存放所有学生数据，每一个学生的数据都是一个列表
while True:
    # 1、界面
    print("---------------------------------------------------------------")
    print("毕业联系方式管理系统")
    print("[1]增加学员信息")
    print("[2]删除学员信息")
    print("[3]退出系统")
    print(("---------------------------------------------------------------"))
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




