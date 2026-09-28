# #write a pgm to check the following
# #a num is divisible by 2 and 3
# #a number is divisile by 2 and not divisble by 3
# # a number is divisible by 3 and not divisible by 2
# #number is not divisble by 2 and 3
# n=int(input())
# if n%2==0:
#     print('divi by 2')
#     if n%3==0:
#         print("divi by 3")
#     else:
#         print("not divi by 3")
# else:
#     print("not divisibe by 2")
#     if n%3==0:
#         print("divi by 3")
#     else:
#         # print("not divi by 3")
#write a pgm to check the enetered numer is psitive even or odd or negatove even or odd
n=int(input())
if n<0:
    print("negative")
    if n%2==0:
        print('neg even')
    else:
        print('neg odd')
else:
    print("positive")
    if n%2==0:
        print('even')
    else:
        print('odd')

