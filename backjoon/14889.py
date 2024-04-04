# 스타트와 링크

def cal(alst,blst):
    asm = bsm = 0
    for i in range(M):
        for j in range(M):
            asm += capa[alst[i]][blst[j]]
            bsm += capa[blst[i]][blst[j]]
    return abs(asm-bsm)

def dfs(n,alst,blst):
    if n == M:
        if len(alst) == len(blst):
            ans = min(ans, cal(alst,blst))
        return
    dfs(n+1,alst+[n],blst)
    dfs(n+1,alst,blst+[n])

N = int(input())
M = N//2
capa = [list(map(int,input().split())) for _ in range(N)]
ans = 10000
dfs(0,[],[])
print(ans)


