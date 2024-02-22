# 풍선팡 보너스 게임
T = int(input())
di = [-1,0,1,0]
dj = [0,-1,0,1]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    score_list = []
    for i in range(N):
        for j in range(N):
            score = arr[i][j]
            for n in range(4):
                for k in range(1, N):
                    mi = i+(di[n]*k)
                    mj = j+(dj[n]*k)
                    if 0<=mi<N and 0<=mj<N:
                        score += arr[mi][mj]
                score_list.append(score)
    
    print(f'#{tc}', max(score_list))



