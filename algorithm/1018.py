# 체스판 다시 칠하기
N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
result = []

for i in range(N-7):
    for j in range(M-7):
        cnt_1 = 0
        cnt_2 = 0
        for k in range(i, i+8):
            for n in range(j, j+8):
                if (k+n) % 2 == 0:
                    if board[k][n] != 'B':
                        cnt_1 += 1
                    if board[k][n] != 'W':
                        cnt_2 += 1
                else:
                    if board[k][n] != 'W':
                        cnt_1 += 1
                    if board[k][n] != 'B':
                        cnt_2 += 1
        result.append(cnt_1)
        result.append(cnt_2)
print(min(result))

      
    