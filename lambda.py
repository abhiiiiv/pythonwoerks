# # # # # #defone a funcion thsat takes a number as argumnet and return a square
# # # # # def sqr(n):
# # # # #     return n**2
# # # # # print(sqr(3))
# # # #
# # # #
# # # #
# # # # # #Using lambda
# # # # a=lambda n:n**2
# # # # print(a(5))
# # # #sum of two numbers
# # # lambda a,b:a+b
# # # #product of 3 numbers
# # # lambda a,b,c:a*b*c
# # # #cube of anumber
# # # lambda a:a**3
# # # #first letter of astring
# # # lambda s:s[0]
# # # #length of a string
# # # lambda s:len(s)
# # # #reverse of string
# # # lambda s:s[::-1]
# # # #name value from a dictionary
# # # lambda d:d.get('name')
# # #
# # # #second elementfrom list
# # # lambda l:l[1]
# # #
# # # #add 10 to anumber
# # # lambda n:n+10
# #
# # #map
# # # 3CREATE A NEW LIST OF SQUres
# # #
# # n=[1,2,3,4]
# # print(list(map(lambda x:x**2,n)))
# # print(tuple(map(lambda x:x**2,n)))
# # print(set(map(lambda x:x**2,n)))
#
# #filter
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))
# #given a list
# l=[23,45,67,89,70]
# #filter the evn values greater than 50
# print(list(filter(lambda x:x%2==0 and x>50,l)))
# #given a list
# colors=['red','green','blue','yellow','orange']
# #filter the colorwhose elength is grater than 5
# print(list(filter(lambda x:len(x)>5,colors)))
# #filter the coloe contaimg letter,n
# print(list(filter(lambda x:'n' in x,colors)))

#reduce

#sum of list
l=[1,2,3,4]
from functools import reduce
print(reduce(lambda x,y:x+y,l))