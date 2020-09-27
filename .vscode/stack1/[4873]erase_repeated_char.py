""" 문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50

다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

[출력]
 
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다. """

def Erase_repeated(char):
    stack = []
    
    while True:
        i = 0
        while i < (len(char)-1):
            if char[i]!=char[i+1]:
                i += 1
            else:
                WP = i
                break
        while(WP):
            for j in range(WP, len(char)):
                if char[WP] != char[j]:
                    EP = j
                    if EP != None:
                        break
            del char[WP:EP]
            WP = None
            EP = None
        
        if i >= (len(char)-1):
            break
    return char

T = int(input())
for test_case in range(1, T+1):
    char = list(map(str, input()))
    Erased = Erase_repeated(char)

    print("#{0} {1}".format(test_case, len(Erased)))