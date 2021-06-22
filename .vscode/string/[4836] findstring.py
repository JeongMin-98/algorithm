def findstring(p, t):
    i = 0 # pattern
    j = 0 # total
    count = 0
    search = True

    for x in range(len(t)):
        j = x
        while i<len(p) and p[i] == t[j] and search :
            i += 1
            j += 1
            if i == (len(p)-1) and p[i]==t[j] :
                count += 1
                x += 1
                i = 0

        if j > len(t): break

    return count

            
T = int(input())

for test_case in range(1,T+1):
    str1 = input()
    str2 = input()

    result = findstring(str1, str2)
    print("#{0} {1}".format(test_case, result))
    