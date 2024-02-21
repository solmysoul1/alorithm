# 색종이
paper = [[0]*100 for _ in range(100)]
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    for i in range(N, N+10):
        for j in range(M, M+10):
            paper[i][j] = 1
cnt = 0
for n in range(100):
    for m in range(100):
        if paper[n][m] == 1:
            cnt += 1

print(cnt)

