# 부분집합의 합

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    result = 0

    for i in range(1<<12):
        sum_sub = 0
        subset = []
        for j in range(12):
            if i & (1<<j):
                sum_sub += arr[j]
                subset.append(arr[j])
        if len(subset) == N and sum_sub == K:
            result += 1

    print(f'#{tc} {result}')



