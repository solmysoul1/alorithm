# N과 M (2)

def dfs(start):
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    
    for i in range(start,N+1):
        if i not in tmp:
            tmp.append(i)
            dfs(i+1)
            tmp.pop()

N, M = map(int,input().split())
tmp = []
dfs(1)