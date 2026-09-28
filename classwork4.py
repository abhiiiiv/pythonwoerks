#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese
# w=float(input('w in kg:'))
# h=float(input('h in m:'))
# BMI=float(w/(h**2))
# print(BMI)
# if BMI<=18.4:
#     print("underweight")
# # elif BMI>=18.5 and BMI<=24.9:
# #     print('Normal')
# # elif BMI>=25.0 and BMI<=39.9:
# #     print('Overweight')
# # elif BMI>=40.0:
# #     print('Obese')
# #2.# A toy vendor supplies three types of toys:
#
# # Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
#
# # The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
#
# # On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,
#
# # and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
#
# # Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.
#
# # Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
#
# toy=int(input())
# cost=int(input())
# if toy==1:
#     print('Battery Based Toy')
#     if cost>=1000:
#         print(f"cost={cost-cost*0.10}")
#     else:
#         print(f"cost={cost}")
# elif toy==2:
#     print('Key Based Toy')
#     if cost >= 100:
#         print(f"cost={cost-cost * 0.05}")
#     else:
#         print(f"cost={cost}")
# elif toy==3:
#     print('electrical charging Based Toy')
#     if cost >= 500:
#         print(f"cost={cost-cost * 0.10}")
#     else:
#         print(f"cost={cost}")
#


#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number
n=int(input())
if n%3==0 and n%5!=0:
    print('fizz')
elif n%5==0 and n%5!=0:
    print('buzz')
elif n%3==0 and n%5==0:
    print('fizzbuzz')
else:
    print(n)