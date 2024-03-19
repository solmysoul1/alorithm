# N과 M (4)

def dfs(start):
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    for j in range(start,N+1):
        tmp.append(j)
        dfs(j)
        tmp.pop()

N, M = map(int, input().split())
tmp = []
dfs(1)