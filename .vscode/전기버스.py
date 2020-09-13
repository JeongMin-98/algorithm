"""

[예시]

다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

[입력]
 
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
M : 충전기가 설치된 정류장 수
N : 전체 정류장 수

"""

T = int(input()) # test_case
for test_case in range(1,T+1):

    K,M,N = map(int, input().split())
    charger = list(map(int, input().split()))

    station = [0]*N

    for i in range(len(charger)):
        station[charger[i]]+=1
    

