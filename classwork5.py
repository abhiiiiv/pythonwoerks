#
#
# # # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# for i in range(1,101,1):
#     if i%3==0 and i%5==0:
#         print(i,end=" ")
# print()
# # # 2.Print the cumulative sum of a list.
# # # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]
# n=int(input('n='))
# q1=[int(input('q1=')) for i in range(n)]
# q12=[]
# sum=0
# for i in q1:
#     sum+=i
#     q12.append(sum)
# print(q12)
#


# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25
# a=int(input('a'))
# b=int(input('b'))
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print(sum)



# 4.Given a list, sum only the elements at even indices.
# l=[10,20,30,40,50]
# # Example:
# #  → Sum = 10 + 30 + 50 = 90
# sume=0
# for i in range(len(l)):
#     if i%2!=0:
#         continue
#     sume+=l[i]
# print(sume)





#5.Given a list, sum the elements until a 0 is encountered (stop at 0).
# l=[4,9,1,0,6,7]
# su=0
# for i in l:
#     su=su+i
#     if i==0:
#         break
# print(su)

# 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
# for i in range(1,1001,1):
#     if i%7==0 and i%11==0:
#         break
# print(i)
# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
# srin=['abhiannd','arju','gautham']
# for i in srin:
#     if len(i)<5:
#         continue
#     print(i)




# 8.From a list of numbers, create a new list containing the squares of each element.
# # Input: [1, 2, 3] → Output: [1, 4, 9]
# a=[1,2,3]
# o=[]
# for i in a:
#     o.append(i**2)
# print(o)


# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"
# sti='hello world'
# for i in sti:
#     if i in 'aeiouAEIOU':
#         continue
#     print(i,end=" ")





#
# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
# l=[5,2,8,6,25]
# l2=[]
# do=0
# for i in l:
#     do=i*2
#     if do<50:
#         l2.append(do)
#     do=0
# print(l2)



# 11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"

# digits="0123456789"
# sti="abc123x7z"
# for i in sti:
#     if i in digits:
#         print(i,end=" ")





# 12.Given a list of strings, create a new list containing the length of each string.
# input=["cat", "banana", ""] #→ Output: [3, 6, 0]
# out=[]
# for i in input:
#     out.append(len(i))
# print(out)

# 13.Given a list of words, create a string made of the first letter of each word.
# input=["Python", "Is", "Great"] #→ Output: "PIG"
# # out=""
# # for i in input:
# #     out=out+i[0]
# # print(out)
#
# # 14.Replace Negative Numbers with 0
# # Given a list of integers, create a new list where all negative numbers are replaced with 0.
# # input=[4, -3, 2, -1]# → Output: [4, 0, 2, 0]
# # out=[]
# # for i in input:
# #     if i<0:
# #         out.append(0)
# #         continue
# #     out.append(i)
# # print(out)
#
# #
# # 15.
# d={101:['Arun',23,'ekm'],
#      102:['Amal',25,'tvm'],
#      103:['Anu',26,'tcr'],
#       104:['Kiran',27,'ekm']}
# #
# # #print all names of students
#
#
# for i in d.values():
#     print(i[0])
#
# #
# # 16.Write a program to print the numbers from 1 to 100.
# # But for multiples of:
# #
# # 3, print “Fizz” instead of the number
# for i in range(1,101,1):
#     if i%3==0:
#         print('fizz',end=" ")
#
# # 5, print “Buzz” instead of the number
#     elif i%5==0:
#         print('buzz',end=" ")
#
# #
# # Both 3 and 5, print “FizzBuzz”
#     elif i%3==0 and i%5==0:
#         print('fizbuzz',end=" ")
#     else:
#         print(i, end=" ")


#
# Otherwise, print the number itself





# Output format example:
# 1, 2, Fizz, 4, Buzz, … , FizzBuzz, …
#
# 17.Write a Python program that prints numbers from 1 to 50:
#     Skip multiples of 5 using continue
# for i in range(1,51):
#     if i%5==0:
#         continue
#     print(i)
#     Stop the loop if the number becomes greater than 40 using break
# for i in range(1,51):
#     if i%5==0:
#         continue
#     if i>40:
#         break
#     print(i)

#
# 18.Write a program to find
#     Reverse of a number(without[::-1])
# n=1234
# n2=''
# for i in str(n):
#     n2=i+n2
# print(n2)
#
# #     count the number of digits in a given number
# print(len(n2))
# #     sum of digits in  a number
# sum=0
# for i in str(n):
#     sum+=int(i)
#
# print(sum)

#Write a program to check whether a number is armstrong number
# n=int(input('n'))
# p=n
# l=len(str(n))
# sum=0
# for i in range(l):
#     d=n%10
#     sum=sum+d**l
#     n=n//10
# # for i in str(n):
# #     sum=sum+(int(i)**l)
# if sum==p:
#     print('armstrong')
# else:
#     print('not armstrong')
#Factors of a nummber
n=int(input('n'))
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=",")
print()