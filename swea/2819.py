# 격자판의 숫자 이어붙이기
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x,path):
    if len(path) == 7:
        result.add(path)
        return
    for i in range(4):
        new_y = y+dy[i]
        new_x = x+dx[i]

        if new_x<0 or new_x>=4 or new_y<0 or new_y>=4:
            continue

        dfs(new_y,new_x,path+maps[new_y][new_x])

T = int(input())
for tc in range(1,T+1):
    maps = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i,j,maps[i][j])

    print(f'#{tc} {len(result)}')