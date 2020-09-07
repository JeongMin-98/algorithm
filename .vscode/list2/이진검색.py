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
    
list = [1,2,3,8,10]

res = binarySearch(list, 2)
print(res)