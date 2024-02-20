# 줄세우기

T = int(input())
result = list(map(int, input().split()))
turn = []
tmp = []

for i in range(T):
    for s in range(result[i]):
        tmp.append(turn.pop())
    turn.append(i+1)
    for t in range(result[i]):
        turn.append(tmp.pop())

for n in turn:
    print(n, end=' ')