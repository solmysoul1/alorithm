# 기지국
di = [1,0,-1,0]
dj = [0,-1,0,1]
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                for t in range(4):
                    ni = i+di[t]
                    nj = j+dj[t]
                    if 0<=ni<n and 0<=nj<n:
                        arr[ni][nj] = 'X'
            elif arr[i][j] == 'B':
                for t in range(4):
                    for s in range(1,3):
                        ni = i+(di[t]*s)
                        nj = j+(dj[t]*s)
                        if 0<=ni<n and 0<=nj<n:
                            arr[ni][nj] = 'X'
            elif arr[i][j] == 'C':
                for t in range(4):
                    for s in range(1,4):
                        ni = i+(di[t]*s)
                        nj = j+(dj[t]*s)
                        if 0<=ni<n and 0<=nj<n:
                            arr[ni][nj] = 'X'
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')


