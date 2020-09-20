T = int(input())

for test_case in range(1,T+1):
    M, N = map(int, input().split()) # M, N 가로 세로 행 M*N
    string = []
    for i in range(M):
        string.append(list(map(str, input())))

    string_T = [[0]*N for i in range(M)]

    for a in range(M):
        for b in range(N):
            string_T[b][a] = string[a][b]

    print(string)
    print("\n")
    print(string_T)