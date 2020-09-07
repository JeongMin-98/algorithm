T = int(input())
for test_case in range(1,T+1):
    arr = [[0]*10 for i in range(10)] # 10*10의 배열판 생성하기
    n = int(input()) # 색칠할 영역 개수 입력받기
    color = []
    purple = 0 # color = 1 red + color = 2 blue이 칠해진 영역의 수
    for j in range(n):
        color.append(list(map(int, input().split()))) # color = [r1,c1,r2,c2,color]
        r = 0
        c = 0                                # 매 과정마다 r,c 초기화 
        for r in range(color[j][0],color[j][2]+1):
            for c in range(color[j][1], color[j][3]+1):
                if arr[r][c] == color[j][4]: 
                    arr[r][c] = arr[r][c] # 색을 칠하려는 색깔이 같으면 칠하지않는다.
                else:
                    arr[r][c] += color[j][4] # 색을 칠하려는 색깔과 다르면 색을 칠한다.  

    for r in range(10):   ## arr 영역에 칠해진 보라색 영역의 개수 구하는 for문
        for c in range(10):
            if arr[r][c] == 3:
                purple += 1
            else:
                continue
    
    print("#{0} {1}".format(test_case,purple))
    
            