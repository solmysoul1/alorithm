def dfs(start):
    node[start] += dfs(start*2) 
    node[start] += dfs(start*2+1)
    
    

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    visited = [[] for _ in range(N+1)]
    node = [[] for _ in range(N+1)]

    for _ in range(M):
        S, T = map(int, input().split())
        node[S] = T

    dfs(1)

