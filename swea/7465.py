# 창용마을 무리의 개수

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        union(s,e)
    cnt = 0
    for i in range(1,N+1):
        if i == parents[i]:
            cnt += 1
    print(f'#{tc} {cnt}')
        
