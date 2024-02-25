# 괄호검사
T = int(input())
for tc in range(1, T+1):
    stack = []
    sen = input()
    result = 0
    for s in sen:
        if s == '(' or s == '{':
            stack.append(s)
        elif s == ')' or s == '}':
            if stack != []:
                if (s == ')' and stack[-1] == '(') or (s == '}' and stack[-1] == '{'):
                    stack.pop()
                else: 
                    break
            else:
                break
    else:
        if stack == []:
            result = 1 

    print(f'#{tc} {result}')
