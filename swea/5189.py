# 전자카트
# path = []

# def EN(x):
#     global min_value
#     if x == N-1:
#         result = [1] + path[:] + [1]
#         value_sum = 0
#         for i in range(N):
#             value_sum += arr[result[i]-1][result[i+1]-1]
#         if min_value > value_sum:
#             min_value = value_sum
#         return
    
#     for i in range(2,N+1):
#         if used[i] == False: 
#             path.append(i)
#             used[i] = True
#             EN(x+1)
#             path.pop()
#             used[i] = False

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     min_value = 10 ** 8
#     used = [False for _ in range(N+1)]
#     EN(0)
#     print(f'#{tc} {min_value}')

def f1(i,k):
    global min_v
    if i == k:
        # p 순서로 방문했을 때의 비용
        s = e[0][p[0]-1] # 사무실에서 첫번째 관리구역
        for j in range(1,k): # 관리구역 사이
            s += e[p[j-1]-1][p[j]-1]
        s += e[p[k-1]-1][0]
        if min_v > s:
            min_v = s

    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[j]
                f1(i+1,k)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N =int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    min_v = 1000
    # 방문 순서를 순열로
    arr = [i for i in range(2, N+1)]
    # 사무실 제외
    used = [0]*(N-1) 
    p = [0]*(N-1)
    f1(0,N-1)

    print(f'#{tc} {min_v}')





