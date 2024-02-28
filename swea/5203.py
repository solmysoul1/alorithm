# 베이비진
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = [0]*10
    p2 = [0]*10
    result = 0
    for i in range(12):
        if i%2 == 0:
            p1[arr[i]] += 1
            if p1[arr[i]] >= 3:
                result = 1
                break
            if 0<=arr[i]-2<10:
                if p1[arr[i]-2]>0 and p1[arr[i]-1]>0 and p1[arr[i]]>0:
                    result = 1
                    break
            if 0<=arr[i]+2<10:
                if p1[arr[i]+2]>0 and p1[arr[i]+1]>0 and p1[arr[i]]>0:
                    result = 1
                    break
            if 0<=arr[i]-1<10 and 0<=arr[i]+1<10:
                if p1[arr[i]-1]>0 and p1[arr[i]]>0 and p1[arr[i]+1]>0:
                    result = 1
                    break
        if i%2 == 1:
            p2[arr[i]] += 1
            if p2[arr[i]] >= 3:
                result = 2
                break
            if 0<=arr[i]-2<10:
                if p2[arr[i]-2]>0 and p2[arr[i]-1]>0 and p2[arr[i]]>0:
                    result = 2
                    break
            if 0<=arr[i]+2<10:
                if p2[arr[i]+2]>0 and p2[arr[i]+1]>0 and p2[arr[i]]>0:
                    result = 2
                    break
            if 0<=arr[i]-1<10 and 0<=arr[i]+1<10:
                if p2[arr[i]-1]>0 and p2[arr[i]]>0 and p2[arr[i]+1]>0:
                    result = 2
                    break
    
    print(f'#{tc} {result}')

# ---------------------------------------------------

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = [0]*10
    p2 = [0]*10
    result = 0
    flag = 0
    for i in range(12):
        if i%2 == 0:
            p1[arr[i]] += 1
            for j in range(8):
                if p1[j]>0 and p1[j+1]>0 and p1[j+2]>0:
                    result = 1
                    flag = 1
                    break
            for s in range(10):
                if p1[s]>=3:
                    result = 1
                    flag = 1
                    break
        if i%2 == 1:
            p2[arr[i]] += 1
            for t in range(8):
                if p2[t]>0 and p2[t+1]>0 and p2[t+2]>0:
                    result = 2
                    flag = 1
                    break
            for k in range(10):
                if p2[k]>=3:
                    result = 2
                    flag = 1
                    break
        if flag == 1:
            break

    print(f'#{tc} {result}')

'''
for 문 안에 있는 for문에만 break 문을 걸어두어서 안쪽 for문이 break 되고도
바깥쪽 for 문이 계속 돌아서 틀린 답이 나옴
이런 경우에는 flag 라는 전역 변수를 하나 만들어서 0으로 초기화 한 후
안쪽 for 문 break 전에 flag = 1 로 바꿔준 후 
바깥쪽 for 문에 if flag == 1: break 라는 조건을 하나 더 생성해서 
바깥쪽 for 문을 멈춰줌
'''

        
