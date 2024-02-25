# 초심자의 회문검사
T = int(input())
for tc in range(1, T+1):
    str = input()
    str_list = []
    result = 0
    for s in str:
        str_list.append(s)
    for s in str:
        if str_list.pop() == s:
            pass
        else:
            break
    else:
        result = 1
    print(f'#{tc} {result}')
