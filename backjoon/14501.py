# 퇴사

# 완전탐색, 백트레킹
# N(종료조건) : 날짜(index)

# def dfs(n, sm):
#     global ans
#     # 종료조건 : 가능한 n을 종료에 관련된 것으로 정의
#     if n>=N:
#         ans = max(ans,sm)
#         return
#     # 하부호출 
#     # 상담하는 경우 (퇴사일 전 완료 가능한 상담)
#     if n+T[n]<=N:
#         dfs(n+T[n],sm+P[n])
#     dfs(n+1,sm)


# N = int(input())
# T = [0] * N
# P = [0] * N
# for i in range(N):
#     T[i], P[i] = map(int, input().split())

# ans = 0
# dfs(0,0)
# print(ans)

# ------------------------------------------- 

# N = int(input()) # 퇴사까지 남은 날
# T = [] # 걸리는 시간
# P = [] # 얻을 수 있는 수익
# dp = [0]*(N+1)
# max_v = 0

# for _ in range(N):
#     x, y = map(int, input().split())
#     T.append(x)
#     P.append(y)

# for i in range(N-1,-1,-1):
#     time = T[i] + i
#     if time <= N:
#         dp[i] = max(P[i] + dp[time], max_v)
#         max_v = dp[i]
#     else:
#         dp[i] = max_v
# print(max_v)

        