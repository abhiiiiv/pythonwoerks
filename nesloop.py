# #given alist
#
# for i in range(1,4):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#
#
# for i in range(1,4):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         print('*',end=" ")
#     print()
#
# for i in range(0,5):
#     for j in range(0,i+1):
#         print('*',end=" ")
#     print()
#
# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)
# for i in range(0,4):
#     for j in range(0,4-i):
#         print('*',end=" ")
#     print()

#given alis
# names=['kelly','alan','jeny']
# for i in names:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#given 2 lists
# n=[1,2,3]
# q=['what','when','why']
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=" ")
#     print()
# given a list
# d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24},{'id':101,'name':'anu','age':25}]
# for i in d:
#     for j in i.values():
#         print(j,end=" ")
#     print()

# for i in range(0,5):
#     for j in range(0,5-i):
#         print('*',end=" ")
#     print()

# for i in range(0,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# for i in range(0,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#
# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# #given a list
# l=[23,45,78,90,12,13,91]
# #print all prime numbers
#
# for i in l:
#
#     for j in range(2,i):
#         if(i%j==0):
#             break
#
#     else:
#         print(i)
#         print('prime')

#find all prime numbers in range (1,100)
# for i in range(1,100):
#     if i>1:
#         for j in range(2, i):
#             if (i % j == 0):
#                 break
#
#         else:
#             print(i)


#find all armstrong numbers i n range (100,1000)

# for i in range(100,1000):
#     l=len(str(i))
#     sum=0
#     for j in str(i):
#         # for k in range(len(j)):
#         sum = sum + (int(j) ** l)
#         if sum == int(i):
#             print(i)

# for i in range(0,4):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
#
# for i in range(0,4):
#     for j in range(1,5-i):
#         print('*',end=" ")
#     print()
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k+1
#
#     print()


# for i in range(1,5):
#     k=ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(j,end=" ")
#         else:
#             print('0',end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print('0',end=" ")
#         elif j%2!=0:
#             print('1',end=" ")
#     print()

# for i in range(1,6):
#
#     for j in range(0,i):
#         print(j,end=" ")
#     print()

# s="hello"
# for i in range(1,6):
#
#     for j in range(0,i):
#         print(s[j],end=" ")
#     print()
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print('*',end="   ")
    k=k-2
    print()

k=2
for i in range(3,0,-1):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print('*',end="   ")
    k=k+2
    print()











