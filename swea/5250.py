from collections import deque

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    visited = [[int(1e9)]*N for _ in range(N)]
    visited[0][0] = 0
    # 도착 비용이 갱신되는 칸을 인큐, 중복될 수 있음
    q = deque()     # 큐 생성, 비용이 갱신된 칸의 인접 인큐(그 칸의 주변도 다시 갱신 될 수 있으므로)
    q.append((0,0))
    while q:
        i, j = q.popleft()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                # 높이 차이에 의한 연료 소비 
                diff = H[ni][nj]-H[i][j] if H[ni][nj] >= H[i][j] else 0
                # 기존보다 연료를 덜 소비하고 도착하면
                if visited[ni][nj] > visited[i][j]+diff+1:
                    q.append((ni,nj))
                    # 새로운 연료 소비량
                    visited[ni][nj] = visited[i][j]+diff+1

    print(f'{tc} {visited[N-1][N-1]}')
