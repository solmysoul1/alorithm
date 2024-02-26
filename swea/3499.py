# 퍼펙트 셔플
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    name = list(input().split())
    new_list = []
    a = 0
    b = N//2+1
    while True:
        new_list.append(name[a])
        a += 1
        new_list.append(name[b])
        b += 1
        if a == N//2+1 or b == N:
            break
    
    print(new_list)

