# 자리배정
di = [-1,0,1,0]
dj = [0,1,0,-1]
C, R = map(int, input().split())
K = int(input())
seat = [[0]*C for _ in range(R)]
step = 0
i, j = R-1, 0

if K > C*R:
    print(0)
else: 
    for n in range(1, R*C+1):
        seat[i][j] = n
        i += di[step]
        j += dj[step]
        if (i<0 or R<=i) or (j<0 or C<=j) or seat[i][j] != 0:
            i -= di[step]
            j -= dj[step]
            step = (step+1)%4
            i += di[step]
            j += dj[step]
            
for i in range(R):
    for j in range(C):
        if seat[i][j] == K:
            print(j+1, R-i)

