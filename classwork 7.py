# #create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda n:n**3,l)))
#
# #create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda n:n**(1/2),l)))
#
# colors=['red','green','blue','yellow','black']
# #create a new list of lengths
# print(list(map(lambda n:len(n),colors)))
# #create a new list of first characters
# print(list(map(lambda n:n[0],colors)))
# #create a new list of last characters
# print(list(map(lambda n:n[-1],colors)))
# #create a new list of reverse of each elemnt
# print(list(map(lambda n:n[::-1],colors)))
#
# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda n:n+10,l)))
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#     {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#     {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]#
# # # create a new list of emails
# print(list(map(lambda d:d['email'],l)))