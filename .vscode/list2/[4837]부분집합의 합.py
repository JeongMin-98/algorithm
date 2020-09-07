T = int(input())

for test_case in range(1,T+1): # test_case
    A = list(range(1,13)) # 1부터 12까지의 숫자를 원소로 가진 집합 A
    N, K = map(int, input().split()) # N개의 원소, 원소의 합이 K
    result =[]
    x = len(A) # 집합 A의 길이 : 12
    for i in range(1 << x): # 비트연산자를 이용하여 부분집합을 구하는 for문
        mylist = ([A[j] for j in range(x) if (i & (1<<j))])
        if (len(mylist)==N) and (sum(mylist)==K): # 부분집합의 N개의 원소와 원소의 합이 K임을 나타내는 조건문
            result.append(mylist)

    count = len(result) 

    print("#{0} {1}".format(test_case, count))
