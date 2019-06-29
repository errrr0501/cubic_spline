#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#create data
list_a = []
list_b = list()
list_c = [1.0, 2.0, 3.0]

tuple_a = (1, 'a', 3.14)

# #快速多行註解ctrl+/(ㄥ)

# #string to list 
list_a = list('cat') #轉型態
print("list_a:", list_a)

#tuple to list
list_b = list(tuple_a)
print("list_b:", list_b)

#================================
 #assign list_d to list_c
list_d = list_c #c，d會變一樣
 
print("list_d:", list_d)
list_d[1] = 'b'

print("list_d[1] <-- 'b'")
print("list_d:", list_d)
print("list_c:", list_c)

#================================
#list_c is a copy of list_b

list_d = list_c.copy()    #複製c但c保持原樣

print("list_d:", list_d)
list_d[1] = 'b'
print("list_d[1] <-- 'b'")
print("list_d:", list_d)
print("list_c:", list_c)

#================================

#using slice[start:end:step]

list_e = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#number below is [i], i = number

print(list_e[::]) # all
print(list_e[1:]) # 1 begin
print(list_e[1:7]) # 1 to 7  
print(list_e[:3]) # 0 to 3
print(list_e[1:7:1]) # 1 to 7 between 1
print(list_e[0:6:2]) # 0 to 7 between 2
print(list_e[::-1]) #-1=count back
print(list_e[-3:2:-1]) # from 6(8-2) count back(-1) to 3 (because of [:2:])
print(list_e[-3::-1]) # from 6 count back
print(list_e[-3::1]) #from 6 count