# 프로세서 연결하기
'''
N : 가로와 세로의 길이
core :
전선 : 
전선은 직선으로만 설치 가능
전선끼리 겹침 불가
가장자리에 위치한 core는 전원이 연결됨
'''

def dfs(depth, cnt, connect):
    pass

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if j == 0 or j == (N-1) or i == 0 or i == (N-1):
                pass
        
            if arr[i][j] == 1:
                q.append([i,j])

    dfs(0,0,0)
                


            