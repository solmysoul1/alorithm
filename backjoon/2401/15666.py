# N과M (12)

def dfs(i):
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return 
    
    for i in range(i,len(li)):
        tmp.append(li[i])
        dfs(i)
        tmp.pop()

N, M = map(int,input().split())
arr = set(map(int, input().split()))
li = []
for n in arr:
    li.append(n)
li.sort()
tmp = []

dfs(0)