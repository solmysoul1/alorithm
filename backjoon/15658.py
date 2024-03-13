# 연산자 끼워넣기 2

def dfs(n,add,sub,mul,div,s):
    global mn,mx
    if n == N:
        if s > mx:
            mx = s
        if s < mn:
            mn = s
        return mn, mx
    
    if add:
        dfs(n+1,add-1,sub,mul,div,s+lst[n])
    if sub:
        dfs(n+1,add,sub-1,mul,div,s-lst[n])
    if mul:
        dfs(n+1,add,sub,mul-1,div,s*lst[n])
    if div:
        dfs(n+1,add,sub,mul,div-1,int(s/lst[n]))

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
mn = int(1e9)
mx = int(-1e9)

dfs(1,add,sub,mul,div,lst[0])
print(mx,mn)