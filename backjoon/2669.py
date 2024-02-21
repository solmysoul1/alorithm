square = list(input().split() for _ in range(4))
square_map = [[0]*100 for _ in range(100)]
for i in square:
    for s in range(int(i[0]),int(i[2])):
        for t in range(int(i[1]),int(i[3])):
            if square_map[s][t] == 0:
                square_map[s][t] = 1

cnt = 0
for n in range(100):
    for e in range(100):
        if square_map[n][e] == 1:
            cnt += 1

print(cnt)
             
