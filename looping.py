# # #while
# #
# #
# # # # #1,2,3,4,5,.....100
# #
# # # # #1,3,5,7,9,11,13,15
# #
# # # #2,4,6,8,10,12
# #
# #
# # # #1,4,7,10,13,16
# #
# # #10,20,30,40,50,60,70,80
# #
# # #
# # # #3,6,9,12,15,18,21
# # #
# # # #5,4,3,2,1
# # #
# # # #8,6,4,2,0
# # #
# # # #100,101,102,.....200
# # #
# # #
# # # #print all 4 digit numbers(1000-9999)
# # # i=1
# # # while(i<=100):
# # #     print(i)
# # #     i+=1
# # #
# # # i=1
# # # while(i<=15):
# # #     print(i)
# # #     i+=2
# # # i=2
# # # while(i<=12):
# # #     print(i)
# # #     i+=2
# # #
# # # i=10
# # # while(i<=80):
# # #     print(i)
# # #     i+=10
# # # i=3
# # # while(i<=21):
# # #     print(i)
# # #     i+=3
# # #
# # # i=5
# # # while(i>=1):
# # #     print(i)
# # #     i-=1
# # #
# # # i=8
# # # while(i>=0):
# # #     print(i)
# # #     i-=2
# # #
# # # i=100
# # # while(i<=200):
# # #     print(i)
# # #     i+=1
# # #
# # # i=1000
# # # while(i<=9999):
# # #     print(i)
# # #     i+=1
# # #
# # # #1,3,5,7,9,11
# # #
# # # i=1
# # # while(i<=11):
# # #     print(i)
# # #     i+=2
# # #
# # # #print those number divisible by 3 in range (1,50)
# # #
# # i=1
# # while(i<=50):
# #     if(i%3==0):
# #         print(i,end=" ")
# #     i+=1
# # print()
# # #print 3 digits numer  taht are divisible 5 a d 7
# # i=100
# # while(i<=999):
# #     if(i%7==0 and i&5==0):
# #         print(i)
# #     i+=1
# # print()#print thost number in range (100,200) which cintaints digit '3'
# # i=100
# # c=0
# # while(i<=200):
# #     if '3' in str(i):
# #         print(i)
# #         c+=1
# #     i+=1
# # # print(c)
# # #sum of serios 1,2,3,4,5,
# # sum=0
# # i=1
# # while(i<=5):
# #     sum=sum+i
# #     i+=1
# # print(sum)
# #
# # pro=1
# # i=1
# # while(i<=5):
# #     pro=pro*i
# #     i+=1
# # print(pro)
# #product of fist 10 ecven numbers
# # c=0
# # pro=1
# # i=2
# # while(c<=10):
# #     if(i%2==0):
# #         pro=pro*i
# #         c=c+1
# #     i+=1
# # print(pro)
#
# i=4
# while(i<=39):
#     print(i)
#     i=i+5
#
# i=1
# sum=0
# while(i<=11):
#     sum=sum+i
#     i=i+2
# print(sum)
#
# i=1
# pro=1
# while(i<=50):
#     if i%3==0 and i%5==0:
#         pro=pro*i
#     i=i+1
# print(pro)
#
# i=100
# cnt=0
# while(i<=999):
#     if i%7==0:
#         cnt=cnt+1
#     i=i+1
# print(cnt)



#factoorial of a njmber
n=int(input('num='))
i=1
fact=1
while(i<=n):
    fact=fact*i
    i=i+1
print(fact)


#multiplication table of  number upto 10
m=int(input())
i=1
p=0
while(i<=10):
    p=m*i
    print(p,'=',m,'*',i)
    i=i+1
print()