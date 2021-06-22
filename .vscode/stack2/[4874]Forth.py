T = int(input())
for test_case in range(1, T+1):
    forth = list(map(str, input().split()))
    stack = []
    result = 0
    a = 0; b=0

    for i in forth:
        if chr(49) <= i and chr(57) >= i: # chr(57):9
            stack.append(i)
        elif i in ['+','-','/','*']:
            if len(stack)>1:
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                if i =='+':
                    stack.append(b+a)
                elif i == '-':
                    stack.append(b-a)
                elif i == '/':
                    stack.append(b//a)
                else:
                    stack.append(b*a)
            else:
                result = 'error'
                break
        else:
            if len(stack)==1:
                result = stack.pop(-1)
                break
            else:
                result="error"
                break
    if not(result):
        result = "error"

    print("#{0} {1}".format(test_case, result))