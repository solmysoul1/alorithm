# 색종이
paper = [[0]*100 for _ in range(100)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for i in range(99-M, 91-M):
        for j in range(N, 10+N):
            if 0<=i<100 and 0<=j<100:
                paper[i][j] += 1
    cnt = 0
    for i in range(100):
        for j in range(100):
            if paper[i][j] == T:
                cnt += 1

print(cnt)
