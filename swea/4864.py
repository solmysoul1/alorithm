# 문자열 비교

T = int(input())
for tc in range(1, T+1):
    s1 = input()
    s2 = input()
    len_s1 = 0
    len_s2 = 0
    result = 0
    for s in s1:
        len_s1 += 1
    for s in s2:
        len_s2 += 1
    for i in range(len_s2-len_s1+1):
        if s2[i:i+len_s1] == s1:
            result = 1
    print(f'#{tc} {result}')