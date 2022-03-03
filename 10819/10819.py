import sys
from itertools import permutations


def get_sum(num_list):
    result = 0
    for idx in range(1,len(num_list)):
        result += abs(num_list[idx-1] - num_list[idx])

    return result


N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

max_diff = 0
for P in permutations(A, N):
    num = get_sum(P)
    max_diff = max(max_diff, num)

print(max_diff)
