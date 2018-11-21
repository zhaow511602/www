#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 1. ###################### 面向对象封装思想 ######################
# user_list = [
#     '孙琦','高腰','走润城','韩增信'
# ]

# user_list = [
#     {'name': '孙琦','age': 18},
#     {'name': '高腰','age': 18},
# ]

# user_list = [
#     dict(name='孙琦',age='18'),
#     dict(name='高腰',age='18'),
# ]

"""
class MyDict(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        return self.name.strip()

user_list = [
    MyDict(name='孙琦',age='18'),
    MyDict(name='高腰',age='18'),
]
for item in user_list:
    item.show()
"""
# 封装： 类中封装了数据，方法
# 职责划分：封装什么就处理什么，目的为其他调用者提供功能
# 应用
# class FilterList(object):
#     def __init__(self,option):
#         self.option =option
#
#     def show(self):
#         self.option.nick()
#
#
# class FilterOption(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def nick(self):
#         tpl = self.name + str(self.age)
#         return tpl
#
#
# FilterList(FilterOption('阮国栋',19))
# FilterList(FilterOption('李志',19))
# FilterList(FilterOption('李杰',19))
# FilterList(FilterOption('李连杰',19))

# 2. ###################### __iter__方法 ######################
"""
class Foo(object):
    def __init__(self):
        pass

    def __iter__(self):
        yield 1
        yield 2
        yield 3
        yield 4

obj = Foo()
for item in obj:
    print(item)
"""
# ###################### 应用 ######################
class FilterList(object):
    def __init__(self,option,data_list):
        self.option =option
        self.data_list = data_list

    def show(self):
        self.option.nick()
    def __iter__(self):
        yield "全部："
        for i in self.data_list:
            yield "<a href='{0}'>{1}</a>".format(i,self.option.bs+i)

class FilterOption(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def nick(self):
        tpl = self.name + str(self.age)
        return tpl
    @property
    def bs(self):
        if self.age > 15:
            return "大"
        else:
            return "小"

obj_list = [
    FilterList(FilterOption('阮国栋',9),["女人",'仙','睡觉']),
    FilterList(FilterOption('李志',19),['阮国栋','走润城']),
    FilterList(FilterOption('李杰',10),['骚浪贱']),
    FilterList(FilterOption('绿城育',18),['吃','喝','嫖','无人机','同学'],),
]

for obj in obj_list:
    for item in obj:
        print(item,end="  ")
    else:
        print('')













