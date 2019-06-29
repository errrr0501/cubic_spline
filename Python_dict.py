#!/usr/bin/env python
# -*- coding: UTF-8 -*-
dict_a = {}
dict_b = dict()
dict_c = {"Key_1": 1, "Key_2": 2.0, "Key_3": "3"}
list_a = ['12','34', '56']
tuple_a = ('ab', 'cd', 'ef')

#字典沒有順序

dict_d = dict(list_a)  #轉型  
dict_e = dict(tuple_a)

print("dict_d.items():", list(dict_d.items()))
print("dict_d.keys():", list(dict_d.keys()))
print("dict_d.values():", list(dict_d.values()))

#=======================

print("dict_c:", dict_c)
print("dict_d:", dict_d)
print("dict_e:", dict_e)

#=======================

print(dict_c["Key_2"])#查字典

dict_c["Key_4"] = 'four'#新增字典內容
print(dict_c["Key_4"])

dict_c["Key_4"] = 'FOUR'#新的字典內容會蓋過舊的
print(dict_c)

#=======================

print("dict_d:", dict_d)
print("dict_e:", dict_e)

#update 2 dict 合併字典
dict_d.update(dict_e)
print("dict_d:", dict_d)

#=======================

print("dict_d:", dict_d)

#delete a item in dict
del dict_d['1']
print("dict_d:", dict_d)

#=======================

dict_f = dict_d
print("dict_d:", dict_d)
print("dict_f:", dict_f)

dict_f['1'] = "Haha! once again!"#字典更改會被更著複製

print("dict_d:", dict_d)
print("dict_f:", dict_f)

#=======================

dict_f = dict_d.copy()
print("dict_d:", dict_d)
print("dict_f:", dict_f)

dict_f['1'] = "Huh..."#用copy就不會

print("dict_d:", dict_d)
print("dict_f:", dict_f)

