# 토마토
from pprint import pprint
from collections import deque
import sys
M, N = map(int, sys.stdin.readline().split())
start = deque()
arr = []
for y in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)
    for x in range(M):
        if tmp[x] == 1:
            start.append([x,y])

dx = [-1,0,1,0]
dy = [0,-1,0,1]

while start:
    x, y = start.popleft()
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if 0<=mx<M and 0<=my<N:
            if arr[my][mx] == 0:
                arr[my][mx] = arr[y][x] + 1
                start.append([mx,my])
result = 0
for i in arr:
    if 0 in i:
        print(-1)
        exit()
    result = max(result, max(i))

print(arr)
print(result-1)




