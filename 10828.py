# 스택
N = int(input())
for tc in range(1, N+1):
    command = [list(input().split()) for _ in range(N)]
    stack = []
for c in command:
    if c == 'push':
        pass
    elif c == int:
        stack.append(c)
    elif c == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c == 'size':
        print(len(stack))
    elif c == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
         

