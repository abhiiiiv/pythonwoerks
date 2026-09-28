# # # Q1.Define a function that takes 2 numbers and returns their product
# n1=int(input())
# n2=int(input())
# def prod(n1,n2):
#     return n1*n2
# x=prod(n1,n2)
# # print(x)
# # # Q2.Define a function that takes a string and returns number of vowels
# def vow(n):
#     vowels=""
#     for i in n:
#         if i in 'aeiouAEIOU':
#             vowels+=i
#     return vowels
# n=input()
# p=vow(n)
# print(p)
# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
# def area(l,b):
#     return l*b
# l=int(input())
# b=int(input())
# a=area(l,b)
# print(a)
#
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
# def even(l):
#     e=[]
#     for i in l:
#         if i%2==0:
#             e.append(i)
#     return e
# a=even(l)
# print(a)

# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
l = [123, 345, 111, 678, 134, 809]
def three(p):
    l1=[]

    for i in p:
        sum = 0
        while i>0:

            k=i%10
            sum=sum+k
            i=i//10
        l1.append(sum)
    return(l1)
a=three(l)
print(a)







#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]
# def uni(l):
#     u=[]
#     for i in l:
#         if i not in u:
#             u.append(i)
#     return u
# a=uni(l)
# print(a)

#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
list1=[12,34,56,78,90]
list2=[90,34,11,57,45]
def com(list1,list2):
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3
a=com(list1,list2)
print(a)
