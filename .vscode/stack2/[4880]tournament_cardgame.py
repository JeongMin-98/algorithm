T = int(input()) 

# 가위 : 1
# 바위 : 2
# 보   : 3

def divideconquer(start, end):
    m = (start+end) // 2
    if start == end:
        return start
    left = divideconquer(start, m)
    right = divideconquer(m+1, end)

    return RSP(left, right)
def RSP(left, right):
    if (card[left] == 1 and card[right]==3):
        return left
    elif (card[left]== 2 and card[right] == 1):
        return left
    elif (card[left]== 3 and card[right] == 2):
        return left
    elif (card[left]==card[right]):
        return left
    else:
        return right
for test_case in range(1, T+1):
    end = int(input())
    start = 0
    end = end - 1
    card = list(map(int, input().split()))

    print("#{} {}".format(test_case, divideconquer(start, end)+1))
