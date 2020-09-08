def binarySearch(a, key):
    start = 1
    end = a
    count = 0
    find = False
    while start <= end and not find:
        middle = (start+end)//2
        count += 1
        if key == middle:
            find = True
        elif key < middle:
            end = middle
        else:
            start = middle
        
    return count

T = int(input())

for test_case in range(1,T+1): # test_case
    P, A, B = map(int, input().split()) # P : 전체 쪽 수, A : A가 찾아야하는 쪽, B : B가 찾아야하는 쪽
    FindA = binarySearch(P, A)
    FindB = binarySearch(P, B)
    if FindA < FindB:
        print("#{0} A".format(test_case))
    elif FindA > FindB:
        print("#{0} B".format(test_case))
    else:
        print("#{0} 0".format(test_case))