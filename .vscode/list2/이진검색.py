def binarySearch(a, key):
    start = 0
    end = len(a)-1
    while start <=end:
        middle = start + (end - start) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return False
    
list1 = list(range(1,400+1))

res = binarySearch(list1, 300)
print(res)