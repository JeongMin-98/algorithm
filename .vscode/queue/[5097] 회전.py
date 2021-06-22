T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())

    data = list(map(int, input().split()))

    result = M%N

    print("#{0} {1}".format(test_case, data[result]))