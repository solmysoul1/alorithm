# 9개의 키를 받아 리스트로 만든 후 오름차순으로 정렬
height_list = [int(input()) for _ in range(9)] 
height_list.sort()
# height_list에서 이중for문을 돌려서 두개의 요소를 추출
for i in height_list:
    for j in height_list:
        # 중복제거
        if i == j:
            pass
        # height_list를 다 더한 값에서 i와 j를 뺀 값이 100일 경우
        elif sum(height_list) - i - j == 100:
            # height_list에서 i와 j를 제거
            height_list.remove(i)
            height_list.remove(j)
            
# height_list 를 순회하며 요소들을 출력
for height in height_list:
    print(height)