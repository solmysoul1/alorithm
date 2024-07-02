# 직사각형

T = int(input())
for tc in range(1, T+1):
    x1, y1, p1, q1 = map(int, input().split())
    x2, y2, p2, q2 = map(int, input().split())
    result = 0
    if x1  > p2 or p1 < x2 or y1 > q2 or q1 < y2:
        result = 4
    elif p1 == x2 or x1 == p2:
        if y1 == q2 or q1 == y2:
            result = 3
        else:
            result = 2
    else:
        result = 1
    print(f'#{tc} {result}')


    
        



