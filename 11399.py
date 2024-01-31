T = int(input())
num = list(map(int, input().split()))
num.sort()

cnt = 0

for i in range(1, T+1):
        cnt += sum(num[:i])

print(cnt)