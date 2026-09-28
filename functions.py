# #sum of two numbers


#define a function to display"hello ur name"
def display():
    n=input("n")
    print("hello",n)
    return
display()
#define a function to find the factorial of a number
def fact():
    prod=1
    n=int(input('n'))
    for i in range(1,n+1):
        prod=prod*i
    print(prod)
    return
fact()
#define a fuction to find the count of a specific character in a givn string
# def count():
#     s="python programing is easy and fun"
#     n=input()
#     cnt=0
#     for i in s:
#         if i in n:
#             cnt=cnt+1
#     print(cnt)
#     return
# count()
#define a function to check whether number is prime or not
# def check():
#     n=int(input('n'))
#     for i in range(2,n):
#         if n%i==0:
#             print('not prime')
#     else:
#         print('prime')
#     return
# check()

#define a functio to find the factors of a number
# def fctrs():
#     n=int(input())
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
#     return
# fctrs()

#parameters and arguments
#sum of t3o numbers
# def add(n1,n2):#paramters
#     s=n1+n2
#     print("sum",s)
#     return
# # add(23,34)#arguments
# a=int(input('a:'))
# b=int(input('b:'))
# add(a,b)

#define a function that takes 3 arguments amount, yaers  and tae as argumets and find the sumpl ineterset avlue
# si=p*n*r/100

# def si(p,n,r):
#     sin=p*n*r/100
#     print(sin)
#     return
# p=int(input('a:'))
# n=int(input('b:'))
# r=int(input('c:'))
# si(p,n,r)

#define a funcciton that takes 2 numbers as arguments and return sum a s result
#call the fuc=nctio n asnd print the resut
#
# def add(n1,n2):
#
#     s=n1+n2
#
#     return s
# a=add(n1,n2)
#define a function that takes a stringaas arugument
#and return a new dictionary where keys are words and vowels are length of each word
#call the fumction and t print the dictionary
# def cnt(s):
#     new={i:len(i) for i in s.split()}
#     return new
# s="python coding is easy and fun"
# a=cnt(s)
# print(a)

#define a function that tajkes a number as argument and chwck whethe thath the number is spy number orn not
# def spy(n):
#     sum = 0
#     prod = 1
#     for i in str(n):
#         sum+=int(i)
#         prod*=int(i)
#     if sum==prod:
#         return "number is spy"
#     else:
#         return "not a spy nymber"
#
# n=int(input())
# a=spy(n)
# print(a)

# def fun(*args):
#     print(args)
# fun(10,20)
# fun(10,20,30)
# fun(1,2,3,4,5)




# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# # print(add(10,20,30))
# def add(*args):
#     pass
# print(add(10,20+))