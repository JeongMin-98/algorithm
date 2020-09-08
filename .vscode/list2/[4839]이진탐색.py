def binarySearch(a, key):
    start = 0
    end = len(a)-1
    count = 0
    find = False
    while not find:
        middle = start + (end - start) // 2
        if key == a[middle]:
            find = True
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
        count += 1
    return count

T = int(input())

for test_case in range(1,T+1): # test_case
    P, A, B = map(int, input().split()) # P : 전체 쪽 수, A : A가 찾아야하는 쪽, B : B가 찾아야하는 쪽
    book = list(range(0,P))
    FindA = binarySearch(book, A-1)
    FindB = binarySearch(book, B-1)
    if FindA < FindB:
        print("#{0} A".format(test_case))
    elif FindA > FindB:
        print("#{0} B".format(test_case))
    else:
        print("#{0} 0".format(test_case))