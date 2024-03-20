# N과 M (11)

def dfs():
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return 
    prev = 0
    for i in range(N):
        if not visited[i] and prev != arr[i]:
            tmp.append(arr[i])
            prev = arr[i]
            dfs()
            tmp.pop()
            visited[i] = 0

N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
visited = [0]*N

dfs()