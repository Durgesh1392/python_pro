def selectionsort(arr):
    # lst[i], lst[minIndex] = lst[minIndex], lst[i]
    for i in range(0, len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)-1):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
if __name__ == '__main__':
   # arr = [2, 3, 5, 4, 1, 8, 6, 7]
    l = eval(input("enter the list"))
    print("Sorted list ")
    selectionsort(l)
    print(l)



