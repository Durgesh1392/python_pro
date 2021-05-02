# linear search algorithm

def search(arr, n, x):

    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
#Driver code

arr = [2, 6, 3, 9, 7, 1, 4, 5]
x = 9
n = len(arr)
# function call
result = search(arr, n, x)
if(result == -1):
    print("the element is not present")
else:
    print("the element is present at index",result)

