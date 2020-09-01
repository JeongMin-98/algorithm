T = int(input()) # test case
for i in range(1,T+1):
    K = int(input())
    N = [0]*K
    # 정수값 입력
    a = map(int, input().split())
    N = list(a)    
    # 정수 리스트 중 최솟값 구하기
    res = max(N)-min(N)
    print('#{0} {1}'.format(i, res))
