# to demonstrate working of array
from array import *
arr = array('i',[])
n = int(input("enter the no of elements you want to enter"))

for i in range(n):
    x = int(input("enter the element"))
    arr.append(x)

print(arr)
val = int(input("enter the value to be searched"))
k=0
for e in arr:
    if val==e:
        print(k)
        break
    k+= 1

print(arr.index(val))
