# 동철이의 일 분배

def dfs(i,sm):
    global max_v
    if sm <= max_v:
        return
    if i == N:
        max_v = max(max_v, sm)
        return 
    
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(i+1,sm*(arr[i][j]/100))
            visited[j] = 0

    

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_v = 0
    visited = [0]*N
    dfs(0,1)
    print(f'#{tc} {max_v*100:.6f}')