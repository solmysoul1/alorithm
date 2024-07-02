def dfs(start):
    visited[start] = 1
    
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)

N, M = map(int, input().split())
visited = [0]*(N+1)
arr = [[] for _ in range(N+1)]
cnt = 0

for _ in range(M):
    U, V = map(int, input().split())
    arr[U].append(V)
    arr[V].append(U)

dfs(1)
print(arr)
print(visited)


