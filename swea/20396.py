# 돌 뒤집기 게임 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    stone = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int,input().split())
        if stone[i-1] == 0:
            for n in range(i-1,i-1+j):
                if 0<=n<N:
                    stone[n] = 0
        elif stone[i-1] == 1:
            for s in range(i-1,i-1+j):
                if 0<=s<N:
                    stone[s] = 1
    
    print(f'#{tc}', *stone)