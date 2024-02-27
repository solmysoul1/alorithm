# 최소합 - 재귀 + 백트래킹
di = [0,1]
dj = [1,0]

def ROUTE(i,j,s):
    if i == N-1 and j == N-1:
        s += arr[i][j]
        total.append(s)
        return
    
    s += arr[i][j]
    
    for n in range(2):
        ni = i + di[n]
        nj = j + dj[n]
        if 0<=ni<N and 0<=nj<N:
            ROUTE(ni,nj,s) 
    else:
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total = []
    arr = [list(map(int, input().split())) for _ in range(N)]
    ROUTE(0,0,0)
    result = min(total)

    print(f'#{tc} {result}')
    
    
    
    