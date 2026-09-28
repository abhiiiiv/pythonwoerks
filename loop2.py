# # # # # # d={'a':10,'b':20,'c':30}
# # # # # # for i in d.values():
# # # # # #     print(i)
# # # # # #
# # # # # # d={'a':10,'b':20,'c':30}
# # # # # # for i in d:
# # # # # #     print(i)
# # # # # # s={1,2,3}
# # # # # # for i in s:
# # # # # #     print(i)
# # # # # # s1='hello'
# # # # # # for i in s1:
# # # # # #     print(i)
# # # # # l=[12,34,56,45,89,16,69,33]
# # # # # #print each numbe ri  alis
# # # # # for i in l:
# # # # #     print(i,end=" ")
# # # # # print()
# # # # # #print even number
# # # # # for i in l:
# # # # #     if i%2==0:
# # # # #         print(i, end=" ")
# # # # # print()
# # # # # #prit number divisiblek by 5
# # # # # for i in l:
# # # # #     if i%5==0:
# # # # #         print(i,end=" ")
# # # # # print()
# # # # # #print numbers with digit 3
# # # # # for i in l:
# # # # #     if '3' in str(i):
# # # # #         print(i,end=" ")
# # # # # print()
# # # #
# # # # # given a stribg
# # # # s='hello world'
# # # # #print each character
# # # # for i in s:
# # # #     print(i,end=" ")
# # # # print()
# # # # #pritn those chaarcters those are not vowels
# # # # v="aeiouAEIOU"
# # # # for i in s:
# # # #     if i not in v:
# # # #         print(i,end=" ")
# # # # print()
# # # #
# # # # # Given a dictionary
# # # # d={'n1':23,'n2':46,'n3':89,'n4':24}
# # # # # print each value
# # # # for i in d.values():
# # # #     print(i)
# # # # # print odd values
# # # # for i in d.values:
# # # #     if i%2!=0:
# # # #         print(i)
# # # # #
# # # # #
# # # # # Given a list
# # # l=["red",'green','orange','blue','black','yellow']
# # # # print each color
# # # for i in l:
# # #     print(i)
# # # # print color starting with 'b'
# # # for i in l:
# # #     if 'b' in i[0]:
# # #         print(i)
# # # # # print color whose length is greater than 5
# # # # for i in l:
# # # #     if len(i)>5:
# # # #         print(i)
# # # #
# # # #
# # # # Given a list
# # # l=[10,'arun','amal',35,3.6,6.9,89]
# # # # print  string values
# # # for i in l:
# # #     if str==type(i):
# # #         print(i)
# # # # print float values
# # # for i in l:
# # #     if float==type(i):
# # #         print(i)
# #
# # l=[45,78,90,12,67]
# # #sum of list
# # sum=0
# # for i in l:
# #     sum=sum+i
# # print(sum)
# # #pro of even
# # pro=1
# # for i in l:
# #     if i%2==0:
# #         pro=pro*i
# # print(pro)
# # #cnt of odd
# # cnt=0
# # for i in l:
# #     if i%2!=0:
# #         cnt+=1
# # print(cnt)
# # print(mul(l))
#
# for i in  range(1,10,2):
#     print(i,end=" ")
# print()
#
# for i in  range(2,11,2):
#     print(i,end=" ")
# print()
#
# for i in  range(4,40,2):
#     print(i**2,end=" ")
# print()
#
# for i in  range(5,0,-1):
#     print(i,end=" ")
# print()
#
# for i in  range(8,-1,-2):
#     print(i,end=" ")
# print()
#
# for i in  range(7,43,7):
#     print(i,end=" ")
# print()

#100,200,..1000
# for i in range(100,1001,1):
#     print(i,end=" ")
# print()
# #1,8,27,64,125
# for i in range(1,5,1):
#     print(i**3,end=" ")
# print()
# #find all 3 digit numbers that are dividible by 3
# for i in range(100,1000,1):
#     if i%3==0:
#         print(i,end=" ")
# print()
# colors=['red','green','blue','yellow','black']
# #printreverse of rach color
# for i in colors:
#     print(i[::-1],end=" ")
# print()

# #print each digit ina number AND sum
# n=1234
# sum=0
# for i in str(n):
#     sum=sum+int(i)
# print(sum)
# l=[1,2,3,4]
# l2=[]
# for i in l:
#     l2.append(i**2)
# print(l2)
#
# s={1,2,3,4}
# s2=set()
# for i in s:
#     s2.add(i**2)
# print(s2)
#given s string
# st="hello world"
# st2=''
#
# for i in st:
#     if i in "aeiouAEIOU":
#         st2=st2+i
# print(st2)
#create a dictionary  sequence where the keys are number and values aare square of each number
# new={1:1,2:4,3:9,4:16}
# new2={}
# for i in new:
#     new2[i]=new[i]
#
# print(new2)
#reverse of a string
# s='hello'
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)

#revers eof a number
# n=1234
# rev=""
# for i in str(n):
#     rev=i+rev
# print(int(rev))