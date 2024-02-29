# 공과 잡초

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    cnt = 0
    l = len(arr)
    for i in range(l):
        if arr[i] in ['(',')']:
            cnt += 1
        if arr[i] == '(':
            if 0<=i+1<l:
                if arr[i+1] == ')':
                    cnt -= 1
        
    print(f'#{tc} {cnt}')

 