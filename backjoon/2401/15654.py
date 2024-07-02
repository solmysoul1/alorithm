# N과 M (5)

def dfs():
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    for i in range(N):
        if not visited[i]:
            tmp.append(arr[i])
            visited[i] = 1
            dfs()
            visited[i] = 0
            tmp.pop()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
tmp = []
visited = [0]*N

dfs()
