# l=[10,20,30,40]
# #key index value numbers
# new={i:l[i] for i in range(0,4)}
# print(new)
# s="hello world"
# for i in s:
#     print(i)
# for i in s.split():
#     print(i)
s="python coding is easy and fun"
#key are words and value are length
new={i:len(i) for i in s.split()}
print(new)