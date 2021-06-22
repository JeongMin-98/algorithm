T = int(input())

def DSF(row, N):
    global subsum
    global result
    if result < subsum:
        return

    if row == N:
        if subsum <= result:
            result = subsum
        else:
            return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            subsum += sell[row][i]
            DSF(row+1, N)
            visited[i] = 0
            subsum -= sell[row][i]

    

for test_case in range(1, T+1):
    N = int(input())
    sell = []
    subsum = 0
    result = 2^30
    visited = [0]*N
    for i in range(N):
        sell.append(list(map(int, input().split())))
    DSF(0,N)
    print("#{0} {1}".format(test_case, result))
