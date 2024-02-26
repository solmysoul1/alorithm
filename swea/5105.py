# 미로의 거리
di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(i, j):
    q = [[i,j]]
    countarr[i][j] = 0
    while q:
        c = q.pop()
        i, j = c[0], c[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=di<N and 0<=dj<N and countarr[ni][nj] == 0:
                q.append([ni,nj])
                countarr[ni][nj] = countarr[i][j] + 1
            if maze[ni][nj] == '3':
                countarr[ni][nj] = countarr[i][j] + 1
                return countarr[ni][nj] - 1 
    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    countarr = [[0]*N for _ in range(N)]
    i = 0
    j = 0
    for s in range(N):
        for t in range(N):
            if maze[i][j] == '2':
                i = s
                j = t

