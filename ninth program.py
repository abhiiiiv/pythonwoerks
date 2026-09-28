#define a list of five colors
#add a new color yellow to the list
#change the second color to black
#print the list in reverse order
#print the second last color
#print the number of colors
l=['violet','blue','pink','red',"orange"]
l.append('yellow')
l[1]='black'
print(l[::-1])
print(l[-2])
print(len(l))