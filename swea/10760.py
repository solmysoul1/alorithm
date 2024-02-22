# 우주선 착륙2
T = int(input())
di = [-1,0,1,0]
dj = [0,-1,0,1]
li = [-1,-1,1,1]
lj = [-1,1,-1,1]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt_list = []
    for i in range(N):
        for j in range(M):
            cnt = 0
            point = arr[i][j]
            for s in range(4):
                mi = i+di[s]
                mj = j+dj[s]
                if 0<=mi<N and 0<=mj<M:
                    if arr[mi][mj] < point:
                        cnt += 1                                     
                ni = i+li[s]
                nj = j+lj[s]
                if 0<=ni<N and 0<=nj<M:
                    if arr[ni][nj] < point:
                        cnt += 1
            cnt_list.append(cnt)
    result = [n for n in cnt_list if n >= 4]
    print(f'#{tc}', len(result))
            


