# 최소 생산 비용

def dfs(i,sm):
    global res
    if sm >= res:
        return
    if i == N:
        res = min(res, sm)
        return
    
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(i+1,sm+arr[i][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 1000000000
    visited = [0]*N
    dfs(0,0)
    print(f'#{tc} {res}')