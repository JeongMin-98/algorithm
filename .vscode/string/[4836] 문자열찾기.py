""" 두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
 

ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
 

ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
 

다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

 """
def find_str(p,t):
    i = 0
    j = 0
    M = len(p)
    N = len(t)
    i = M - 1
    j = 0
    skip = list(reversed(p))
    while j<N:
        if t[j] == p[i]:
            if t[j] in skip:
                if skip.index(t[j])==0:
                    if t[j+1-M:j+1]==p:
                        return 1
                    else:
                        return 0
            else:
                j += M
        else:
            if t[j] in skip:
                j += skip.index(t[j])
            else:
                j += M
    return 0
    
T = int(input())

for test_case in range(1, T+1):
    pattern = input()
    total = input()

    result = find_str(pattern, total)
    print("#{0} {1}".format(test_case, find_str(pattern,total)))

