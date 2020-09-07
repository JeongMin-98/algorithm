T = int(input())

for test_case in range(1,T+1): # test_case
    A = list(range(1,13)) # 1부터 12까지의 숫자를 원소로 가진 집합 A
    N, K = map(int, input().split()) # N개의 원소, 원소의 합이 K
    result =[]
    x = len(A)
    for i in range(1 << x):
        mylist = ([A[j] for j in range(x) if (i & (1<<j))])
        if (len(mylist)==N) and (sum(mylist)==K):
            result.append(mylist)

    count = len(result) 

    print("#{0} {1}".format(test_case, count))
