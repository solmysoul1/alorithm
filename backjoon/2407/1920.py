# 수 찾기
# 이진 탐색

'''
n개의 정수 중에서 x 라는 정수가 존재하는지 알아내는 프로그램
'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
x_list = list(map(int, input().split()))

for x in x_list:
    pl = 0
    pr = N-1

    while True:

        pc = ( pl + pr ) // 2

        if arr[pc] == x:
            print('1')
            break
        
        elif arr[pc] < x:
            pl = pc + 1

        else:
            pr = pc - 1

        if pl > pr:
            print('0')
            break

    

