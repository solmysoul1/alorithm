# 숫자카드
T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    total = []
    for n in range(max(arr)+1):
        total.append(arr.count(n))
    max_cnt = max(total)
    max_idx = 0
    max_num = 0
    for i in range(max(arr)+1):
        if total[i] >= max_num:
            max_num = total[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_cnt}')