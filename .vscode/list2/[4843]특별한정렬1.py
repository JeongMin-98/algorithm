T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 집합의 개수
    mylist = [0]*N
    mylist = list(map(int, input().split()))

    uniquelist = [0]*N

    for i in range(len(mylist)):
        if mylist[i] == max(mylist):
            