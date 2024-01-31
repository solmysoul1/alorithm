N, M, K = map(int, input().split())

count = 0

for i in range(1, M+1):
    if (N-2 >= 0) and (M-1 >= 0) and (N+M-3) >= K:
        count += 1
        N -= 2
        M -= 1
    else:
        pass

print(count)