# for i in range(1,6):
#     if(i==3):
#         break
#     print(i)
# else:
#     print('hello')

#check whether the number is prime or not
num=int(input('n'))
if num>1:
    for i in range(2, num):
        if (num % i == 0):
            print('not prime')
            break
    else:
        print("prime")
else:
    print('number is neither prime nor composite')
