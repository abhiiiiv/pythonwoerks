# #write a program to create  alist 5 random 3 digit numberds
# import random
# for i in range(0,5):
#     print(random.randint(100,999))
# #write a program to create a 5 digit rasndom otp number
# print(random.randint(10000,99999))
# #write a profeam to find the position of character in a string
# s="hello world"
# print(s.find('o'))
# #define a functon thst a string as a rgumnt and returns a new dictionary
# def sri(s):
#
#     new_dict = {}
#
#     for char in s:
#         if char not in new_dict:
#             new_dict[char] = s.count(char)
#
#
#
#     return new_dict
# s="hello"
# a=sri(s)
# print(a)
#
# #where keys are characyers and values are count of each number
#
# # define a function that takes string as argument and print the cout of digitds ,spaces letter in the string
# def cnt(s):
#     digits = 0
#     spaces = 0
#     letters = 0
#
#     for char in s:
#         if char.isdigit():
#             digits += 1
#         elif char.isspace():
#             spaces += 1
#         elif char.isalpha():
#             letters += 1
#
#     print(f"Digits: {digits}")
#     print(f"Spaces: {spaces}")
#     print(f"Letters: {letters}")
# s="Python programming is easy and fun"
# cnt(s)


#given a string
l=[1,2,2,3,4,5,6]
#create a new dictionary whwerre keys are numbers and values are number occurence of each number
# def cnt(l):
#     new={}
#     for i in l:
#         if i not in new:
#             new[i]=l.count(i)
#     return new
# print(cnt([1,2,2,3,4,5,6]))
#given a list
l=[11,34,78,23,90,65]
# #find the largest number
# print(max(l))
# #find the secong largest
# l.sort()
# print(l[-2])
#
#
# #find the smallest number
# print(min(l))
# #find the secong smallest
# print(l[1])
# s=l.index(max(l))
# l.pop(s)
# print(max(l))

#given a list
# l=[['arun',23,30000],['amal',25,50000],['anu',27,40000]]
# m=[]
# mn=[]
# for i in l:
#     m.append(i[2])
#     mn.append(i[1])
# print(max(m))
# print(min(mn))
#
# l=[23,45,67,12,90,78]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)
#
# max=l[0]
# for i in l:
#     if i<max:
#         max=i
# print(max)

#given a list
# l=[1,1,2,3,3,4]
# print(set(l))
# l=[1,1,2,3,3,4]
# l2=[]
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(sorted(l2))
#
# #3
# l1=[13,27,30,42,57]
# l2=[13,57,89,33,80]
# l1=set(l1)
# l2=set(l2)
# print(l1.intersection(l2))

#