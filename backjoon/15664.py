# N과 M (10)

def dfs(start):
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return 
    prev = 0
    for i in range(start,N):
        if not visited[i] and prev != arr[i]:
            tmp.append(arr[i])
            prev = arr[i]
            dfs(i+1)
            tmp.pop()

N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
visited = [0]*N

dfs(0)