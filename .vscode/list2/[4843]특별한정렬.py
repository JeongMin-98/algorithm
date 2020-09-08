T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    mynumber = [0]*N
    mynumber = list(map(int, input().split()))
    mynumber.sort() #오름차순으로 정렬
    result = [0]*N
    bignum = []
    smallnum = []
    mid = N - N //2
    bignum = mynumber[mid:len(mynumber)]
    bignum.sort(reverse=True)
    smallnum = mynumber[0:mid]
    for k in range(0, mid):  
        result[2*k] += bignum[k]
        result[2*k+1] += smallnum[k] ## 홀수일때 오류나는거 해결할것
    print(result)
