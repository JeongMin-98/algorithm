"""
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.

다음은 5x5 미로의 예이다.

13101

10101

10101

10101

10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
 
[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50 

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

"""


def issafe(y,x):
    return 0 <= x < N and 0 <= y < N and (maze[y][x] == 0 or maze[y][x] == 3)

def FindRoutes(y,x):
    result = 0
    if maze[y][x]==3:
        result = 1
        return result
    visited.append((x, y))
    for dir in range(4):
        New_x = x + dx[dir]
        New_y = y + dy[dir]
        if issafe(New_y, New_x) and (New_y, New_x) not in visited:
            FindRoutes(New_y, New_x)

    
T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 미로의 크기 N
    maze = []
    maze_arr = [] # 미로의 통로와 벽에 대한 정보
    visited = [] # 방문한 미로의 좌표값
    result = 0

    # 상, 하, 좌, 우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for j in range(N):
        maze_arr = (list(map(int, input())))
        maze.append(maze_arr)
    for y in range(N):
        for x in range(N):
            if(maze[y][x]==2):
                y_start = y
                x_start = x
    result = FindRoutes(y_start, x_start)

    print("#{}: {}".format(test_case,result))
