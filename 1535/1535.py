import sys

from itertools import combinations, product

health = 0
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
J = list(map(int, sys.stdin.readline().split()))
LJ = list(zip(L, J))
max_j = 0
for i in range(1, N+1):
    comb = list(combinations(LJ, i))
    for lj in comb:
        if sum([l[0] for l in lj]) < 100:
            max_j = max(sum([l[1] for l in lj]), max_j)

print(max_j)
