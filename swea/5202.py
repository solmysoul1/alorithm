# 화물도크
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = []
    cnt = 1
    for _ in range(N):
        s, e = map(int, input().split())
        schedule.append((s,e))
    schedule.sort(key = lambda x : x[1])
    start = schedule[0][1]
    for s,e in schedule:
        if start<=s:
            cnt += 1
            start = e
    print(f'#{tc} {cnt}')

