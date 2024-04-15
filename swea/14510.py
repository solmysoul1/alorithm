# 나무 높이

'''
A형 시험 회고

bfs로 풀려고 했는데 
물을 안주고 넘어가는 경우를 구현하지 못해서 
4번째 tc에서 계속 틀린 값 반환

적당한 조건에 가지치기를 못해서
recursion error 발생
'''

'''
그리디로 풀기
짝수날의 수와 홀수날의 수로 최적의 날짜 계산

풀이를 보니 규칙을 찾아서 각 경우에 수에 대한
최적의 날짜 규칙을 적용함
'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    trees = list(map(int, input().split()))

    max_height = max(trees)     # 가장 긴 나무의 높이
    total_gap = 0           # 자라야하는 총 나무의 높이
    
    # for 문을 돌려 total_gap 구하기
    even = 0
    odd = 0
    for tree in trees:
        gap = max_height - tree
        even += gap // 2
        odd += gap % 2

    # odd = 0     # 홀수 날의 수
    # even = 0    # 짝수 날의 수 
    # even += total_gap // 2 
    # odd += total_gap % 2
    
    # 규칙에 따르면
    # 짝수 날이 더 많을 경우에는
    # 짝수 날과 홀수 날의 차이가 1 이하여야함
    # 짝수 날과 홀수 날의 개수 맞추기
    
    if even > odd: 
        while abs(even-odd) > 1:
            even -= 1
            odd += 2

    result = 0

    # 아래 코드들도 규칙에 따른 조건문
    if odd > even:
        result = odd*2-1
    
    elif even > odd :
        result = even*2
    
    else:
        result = odd+even
    
    print(f'#{tc} {result}')



