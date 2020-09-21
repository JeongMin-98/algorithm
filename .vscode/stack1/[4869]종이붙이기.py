# 10의 배수인 N이 주어졌을 때, 
# 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오. 
# 직사각형 종이가 모자라는 경우는 없다.

# 가로 10 세로 20 사각형 A => 세로 10 가로 20
# 가로 20 세로 20 사각형 B
def paper(x):
    if x == 1:
        return 1
    if x == 2:
        return 3
    else:
       return (paper(x-1)+2 * paper(x-2))
T = int(input()) # test_case 입력 

for test_case in range(1,T+1): # test_case 만큼 반복
    
    N = int(input()) # 10의 배수 N # ex) N이 30이면 세로 20 가로 30인 직사각형을 A,B를 통해 채우기

    memo =[1,3]
    if N % 10 == 0 and N >= 10 and N <= 300:
        x = int(N/10)
    else:
        print("N은 10의 배수가 아닙니다.")

    print("#{0} {1}".format(test_case, paper(x)))

    