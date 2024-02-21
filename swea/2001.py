# 파리퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_max = 0
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            total = 0
            for s in range(i, i+M):
                for t in range(j, j+M):
                    total += arr[s][t]
        
                if total > total_max:
                    total_max = total
    print(f'#{tc} {total_max}')

                
