# #Create a package named Shapes containing modules circle.py  and
# rectangle.py

#define functions to calculate the area and perimeter of  circle and rectangle.
def carea():
    r=int(input('r'))
    a=3.14*(r**2)
    print(a)

def cperi():
    r=int(input('r'))
    a=3.14*2*r
    print(a)
# write a program mymodule.py to import all these functions from the circle and
# rectangle modules and perform required operations.