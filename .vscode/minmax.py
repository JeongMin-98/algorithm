T = int(input()) # test case
while T > 0:
    
    N = int(input()) #case마다 입력되는 갯수
    N = [0]*N
    # 정수값 입력
    for i in range(len(N)):
        N[i] = int(input())
    
    # 정수 리스트 중 최솟값 구하기
    min = N[0]
    for i in range(len(N)):
        if min<N[i]:
            min = min
        else:
            min = N[i]
    
    # 정수 리스트 중 최댓값 구하기
    max = N[0]
    for i in range(len(N)):
        if max>N[i]:
            max = max
        else:
            max = N[i]
    result = max - min
    print(result)
    T -=1

