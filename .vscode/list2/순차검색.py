def sequentialSearch(a,n,key):
    i = 0
    while i < n and a[i]!=key:
        i = i+1

    if i < n : return i
    else: return -1

list = [1,2,3,4,5]

result = sequentialSearch(list, 5,5)

print(result)