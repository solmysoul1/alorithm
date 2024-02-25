# 달팽이 숫자
T = int(input())
di = [0,1,0,-1]
dj = [1,0,-1,0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    i = j = 0
    arr[i][j] = 1
    direction = 0
    input_v = 1
    while input_v < N**2:
        ni = i + di[direction]
        nj = j + dj[direction]
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] == 0:
                i = ni
                j = nj
                input_v += 1
                arr[i][j] = input_v
            else:
                direction = (direction+1)%4
        else:
            direction = (direction+1)%4
    print(f'#{tc}')
    for i in arr:
        print(*i)

  


    