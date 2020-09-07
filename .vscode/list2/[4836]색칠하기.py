T = int(input())
for test_case in range(1,T+1):
    arr = [[0]*10 for i in range(10)] # 10*10의 배열판 생성하기
    n = int(input()) # 색칠할 영역 개수 입력받기
    color = []
    for j in range(n):
        color.append(list(map(int, input().split())))
    