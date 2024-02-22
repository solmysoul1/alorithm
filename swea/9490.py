T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1,0,1,0]
    dj = [0,-1,0,1]
    score_list = []
    for i in range(N):
        for j in range(M):
            score = arr[i][j]
            for t in range(1,arr[i][j]+1):
                for s in range(4):
                    mi = i+di[s]*t
                    mj = j+dj[s]*t
                    if 0<=mi<N and 0<=mj<M:
                        score += arr[mi][mj]
            score_list.append(score)
    print(f'#{tc}', max(score_list))
                    