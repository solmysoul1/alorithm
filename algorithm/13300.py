# 방배정
N, K = map(int, input().split())
grade_num = [[0,0] for _ in range(7)] # 학년별 여자, 남자학생의 수를 리스트로 저장
for info in range(N):
    S, Y = map(int, input().split())
    grade_num[Y][S] += 1
    # 1학년 남.여 학생의 수는 grade_num의 1번 인덱스에 저장하는 방식
cnt = 0
for i in range(7):
    for j in range(2):
        cnt += grade_num[i][j]//K # 몫을 cnt에 더해주고
        if grade_num[i][j]%K != 0: # 나머지가 0이 아니라면 1을 더 더해줌
            cnt += 1
print(cnt)
