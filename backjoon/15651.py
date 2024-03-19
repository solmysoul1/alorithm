# N과M (3)

def dfs(i):
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    for j in range(1,N+1):
        tmp.append(j)
        dfs(i+1)
        tmp.pop()

N, M = map(int,input().split())
tmp = []
dfs(0)