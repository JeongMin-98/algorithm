def findstring(p, t):
    i = 0
    j = 0
    M = len(p) # M : pattern의 길이
    N = len(t) # N : 전체 string의 길이
    i = i + M - 1
    j = j + M - 1 # i : pattern index, j = str(t) index
    pp = 0
    count = 0
    skip = list(reversed(p))
    while j<N:
        
        if t[j] == p[i]:
            for x in range(M):
                if skip[x] == t[j]:
                    j -= 1
                    pp += 1
                else:
                    break
            if pp == M:
                count += 1
            j = j + pp + 1
        else:
            if t[j] in skip:
                for x in range(M):
                    if t[j] == skip[x]:
                        j += x
            else:
                j += M
    
    return count

T = int(input())

for test_case in range(1,T+1):

    pattern = input()
    total = input()

    count = findstring(pattern, total)
    print("#{0} {1}".format(test_case, count))