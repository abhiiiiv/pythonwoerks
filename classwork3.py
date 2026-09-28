# # #Write a program to check whether two entered numbers are equal or not
n=int(input('n:'))
m=int(input('m:'))
if n==m:
    print('equal')
else:
    print('not equal')
# #Write a program to check whether two entered words are equal or not
word1=input('word1:')
word2=input('word2')
if word1==word2:
    print('w equal')
else:
    print('w not equal')
# #Write a program to find the maximum of two numbers
if n>m:
    print('n is largest')
elif n<m:
    print('m is largest')


# #write a program to check whether the entered character is vowel or not
chr=input()
if 'a' or 'e' or 'i' or 'o' or 'u' in chr:
    print('vowel')
else:
    print('not vowel')
# ch=input("enter your character")

# #Write a program to check whether the entered country name contains word 'land'
country=input()
if land in country:
    print("present")
else:
    print('not present')
# #write a program to check whether the entered number is 3 digit or not
w1=int(input())
if w1>=100 and w1<=999:
    print('3 digit')
else:
    print('not 3 digit')




# #write a program to check whether the entered string is  palindromde or
p1=input('p1')
p2=p1[::-1]
if p1==p2:
    print('palindrome')
else:
    print('not palindrome')

#Write a program to check whether a number is present in given list
l=[23,67,12,90]
l2=int(input())
if l2 in l:
    print('present')
else:
    print('not present')
#Write a program to check whether a key is prsent in a dictionary or not
d={101:'Arun',102:'Amal',103:'Anu'}
d2=int(input())
if d2 in d:
    print('present')
else:
    print('not present')
# #Write a program to check whether the given password is strong/weak(if length lessthan 8 weak)
password=int(input())
if len(password)==8:
    print('strong')
else:
    print('weak')