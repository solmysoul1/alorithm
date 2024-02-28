# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     box = list(map(int, input().split()))
#     truck = list(map(int, input().split()))

#     # 크키별로 내림차순 
#     box.sort(reverse=True)
#     truck.sort(reverse=True)
#     total = 0
#     while box and truck: # 컨테이너와 트럭 모두 남아있으면
#         if box[0] <= truck[0]: # 가장 큰 트럭이 가장 큰 컨테이너를 옮길 수 있으면
#             total += box.pop(0)
#             truck.pop(0)
#         else: # 옮길 수 없으면
#             box.pop(0) # 무거운 화물 하나 포기
#     print(f'{tc} {total}')

# ---------------------------------------------

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    goods = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    goods.sort(reverse=True)
    truck.sort(reverse=True)
    total = 0
    while goods and truck:
        if goods[0] <= truck[0]:
            total += goods.pop(0)
            truck.pop(0)
        else:
            goods.pop(0)
            
    print(f'#{tc} {total}')



