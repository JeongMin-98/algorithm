def factorial(x):
    if x>0:
        if x > 1:
            return x*factorial(x-1)
        else:
            return 1
    else:
        return "팩토리얼 함수를 실행시킬수 없습니다."


x = 0
result = factorial(x)

print(result)