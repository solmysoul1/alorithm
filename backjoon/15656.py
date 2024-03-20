# N과 M (7)

def dfs():
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return 
    for i in range(N):
        tmp.append(arr[i])
        dfs()
        tmp.pop()

N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
dfs()