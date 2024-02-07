import sys
from itertools import combinations

input = sys.stdin.readline
N, S = map(int, input().split())
num_list = list(map(int, input().split()))

subset = 0

for i in range(1, N+1):
    comb = combinations(num_list, i)

    for j in comb:
        if sum(j) == S:
            subset += 1

print(subset)