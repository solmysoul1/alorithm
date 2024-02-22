# 파리퇴치3
T = int(input())
di = [-1,0,1,0]
dj = [0,-1,0,1]
li = [-1,-1,1,1]
lj = [-1,1,-1,1]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_list = []
    for i in range(N):
        for j in range(N):
            total1 = arr[i][j]
            total2 = arr[i][j]
            for s in range(1,M+1):
                for t in range(4):
                    mi = i+(di[t]*s)
                    mj = j+(dj[t]*s)
                    if 0<=mi<N and 0<=mj<N:
                        total1 += arr[mi][mj]
                    ni = i+(li[t]*s)
                    nj = j+(lj[t]*s)
                    if 0<=ni<N and 0<=nj<N:
                        total2 += arr[ni][nj]
            total_list.append(total1)
            total_list.append(total2)
    print(max(total_list))
                    
