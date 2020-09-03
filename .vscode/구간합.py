T = int(input()) # test_case
for test_case in range(1,T+1):
    N, M = map(int, input().split()) # N : 정수의 개수, M : 구간의 개수
    number = [0]*N
    number = list(map(int, input().split())) # N개의 정수 입력받기

    result = []
    for j in range(N-M+1):
        result.append(sum(number[j:j+M]))
    
    print("#{0} {1}".format(test_case, max(result)-min(result)))