#1Given a string
s="I am learning Python"

# find the length of the string
print("1",len(s))
#
# find the reverse of the string
print("2",s[::-1])

# find the last character of the strings
print("3",s[-1])
#find the 13th character
print("4",s[12])
#print the characters from 2nd index to 15 th index
print('5',s[2:16])
#combines the string s with word "programming"
c=s+"programming"
print("6",c)

# #2.Given a string s="python is a programming language"

# #Remove the first 10 characters and print the remaining
print("2.1",s[12::])
# #print the last 5 characters
print("2.2",s[-5])