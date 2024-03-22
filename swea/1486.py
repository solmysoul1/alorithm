# 장훈이의 높은 선반

def dfs(cnt,sum_height):
    global ans
    if sum_height >= B:
        ans = min(ans, sum_height)
        return
    
    if cnt == N:
        return
    
    dfs(cnt+1,sum_height+arr[cnt])
    dfs(cnt+1,sum_height)

T = int(input())
for tc in range(1,T+1):
    N,B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    dfs(0,0)
    print(f'#{tc} {abs(ans-B)}')


