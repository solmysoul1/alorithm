# 고대유적
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    len_list = []
    for i in range(N):
        len1 = 0
        len2 = 0
        if arr[i][0] == 1:
            len1 += 1
        if arr[0][i] == 1:
            len2 += 1
        for j in range(1,M):
            if arr[i][j] == 1:
                len1 += 1
                if j == M-1:
                    len_list.append(len1)
            if arr[i][j] == 0:
                if len1 >= 2 :
                    len_list.append(len1)
                len1 = 0
            if arr[j][i] == 1:
                len2 += 1
                if j == M-1:
                    len_list.append(len2)
            if arr[j][i] == 0:
                if len2 >= 2:
                    len_list.append(len2)
                len2 = 0
    print(f'#{tc}', max(len_list))

