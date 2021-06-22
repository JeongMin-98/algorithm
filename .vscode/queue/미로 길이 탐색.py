from queue import Queue

def issafe(y,x):
    return 0 <= x < size and 0 <= y < size and (maze[y][x] == 0 or maze[y][x] == 3)

def FindRoutes(y,x):
    result = 0
    item = 0
    if maze[y][x]==3:
        result = 1
        return result
    visited.append((x, y))
    queue.put((x,y))
    for dir in range(4):
        New_x = x + dx[dir]
        New_y = y + dy[dir]
        if issafe(New_y, New_x):
            if (New_y, New_x) not in visited:
                FindRoutes(New_y, New_x)
            else:
                queue.get()
                return 0

T = int(input())

for test_case in range(1,T+1):
    size = int(input())
    maze = []
    visited = []
    queue = Queue()

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(size):
        maze.append(list(map(int, input())))

    for y in range(size):
        for x in range(size):
            if(maze[y][x]==2):
                y_start = y
                x_start = x
    result = FindRoutes(y_start, x_start)
    
