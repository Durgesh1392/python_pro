# to reverse array element
from array import *
n = int(input("number of elements"))
x = array('i',[])
for i in range(n):
    y = int(input("enter the elements"))
    x.append(y)
print(x)
for i in range(n,0,-1):

    print(i)
