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
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end="   ")#space differece
#     k=k-2
#     print()
#
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end="   ")#space differece
#     k=k+2
#     print()
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end="   ")#space differece
#     k=k-2
#     print()
#
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end="   ")#space differece
#     k=k+2
#     print()

# k=5
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")#space differece
#     k=k-1
#     print()
k=6
for i in range(1,5):
    for j in range(5-i,0,-1):
        print(end="  ")
    for p in range(1,i+1):
        print('*',end="   ")
    print()
for i in range(1, 4):
    for p in range(0,i+1):
        print(end="  ")
    for j in range(4-i,0,-1):
        print('*',end="   ")

    print()