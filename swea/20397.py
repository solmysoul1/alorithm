# 돌 뒤집기 게임2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    stone = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int,input().split())
        for n in range(1,j+1):
            if 0<=i-1-n<N and 0<=i-1+n<N:
                if stone[i-1-n] == stone[i-1+n]:
                    if stone[i-1-n] == 0:
                        stone[i-1-n],stone[i-1+n] = 1,1
                    elif stone[i-1-n] == 1:
                        stone[i-1-n],stone[i-1+n] = 0,0
    
    print(f'#{tc}', *stone)
               
                    


                    
