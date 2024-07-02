# N과 M (6)

def dfs(start):
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return 
    for i in range(start,N):
        tmp.append(arr[i])
        dfs(i+1)
        tmp.pop()

N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
dfs(0)