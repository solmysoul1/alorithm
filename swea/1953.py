# 탈주범 검거
'''
1 : 상하좌우
2 : 상하
3 : 좌우
4 : 상우
5 : 하우
6 : 하좌
7 : 상좌

N : 세로 M : 가로
R : 뚜껑의 세로 C : 뚜껑의 가로
L : 소요시간
'''
direction = [(0,-1,0,1),()]

def bfs(r,c,n,cnt):
    global count
    if n == L:
        return
    if tunnel[r][c] == 1:


T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    bfs(R,C,1,0)
    print(f'#{tc} {count}')