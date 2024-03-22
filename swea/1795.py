# 인수의 생일파티 

def dij(s, N, adj, D): # X 출발점, N 마지막노드, adj 참고할 인접행렬, D 최소비용테이블
    U = [0]*(N+1)       # U = {s}       # 비용이 결정된 노드의 집합, s 출발점
    U[s] = 1
    for _ in range(N-1):    # 출발점을 제외한 나머지 정점 만큼 반복. while U!=V
        # V-U 원소중에서 D[w]가 최소인 정점 w선택
        min_w = INF     # 최소비용
        w = 0           # D[w]가 최소인 정점 w
        for i in range(1, N+1):
            if U[i]==0 and min_w > D[i]:
                min_w = D[i]
                w = i

        U[w] = 1            # V-U 원소중에서 D[w]가 최소인 정점 w를 U에 포함
        # w에 인접한 정점에 대해, 기존 비용과 w를 거쳐가는 비용을 비교
        for i in range(1, N+1):
            if 0<adj[w][i]<INF:
                D[i] = min(D[i], D[w]+adj[w][i])

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())     # N개의 집, M 도로 수,  X 인수의 집

    INF = 1000000

    adj1 = [[INF]*(N+1) for _ in range(N+1)]   # 인접행렬, 인수의 집에서 귀가하는 최단 거리구하기 용, adj[i][j]는 i에서 j로 가는 시간

    for i in range(N+1):    # 자기집인 경우 귀가시간 0
        adj1[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c

    D1 = [0]*(N+1)  # X에서 각자의 집으로 귀가하는 시간 저장용
    for i in range(1, N+1):
        D1[i] = adj1[X][i]          # 초기 그래프에서 X에서 각 정점까지의 거리(비용)

    dij(X, N, adj1, D1)
    print(D1)