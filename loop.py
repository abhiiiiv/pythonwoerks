#write a prgram to check whether th euser enterd number is 2 digit/3digit/4didgit
n=int(input())
if n>=10 and n<=99:
    print('2 digit')
elif n<=100 and n>=999:
    print('3 digit')
elif n<=1000 and n>=9999:
    print('4 digit')
    #wite a program to print no. of days in a month
    l1=['January','March','May','July','August','October','December']
    l2=['April','June','September','November']
    l3=['February']
    if month in l1:
        print("31")
    if month in l2:
        print('30')
    if month in l3:
        print('28')
#write a pgm for calcukator
n1=int(input())
n2=int(input())
op=input()
if op=='+':
    print(f"sum is:{n1+n2}")
if op=='-':
    print(f"difference is {n1-n2}")
if op=='*':
    print(f" product is {n1*n2}")
if op=='%':
    print(f"modulus is {n1%n2}")
if op=='/':
    print(f"quotient is {n1/n2}")
if op=='//':
    print(f"quotient is {n1//n2}")
#grades
gr=int(input())
if gr>=91 and gr <=100:
    print('A')
elif gr>=81 and gr <=90:
    print('B')
elif gr>=71 and gr <=80:
    print('C')
elif gr>=61 and gr <=70:
    print('D')
elif  gr <61:
    print('E')

