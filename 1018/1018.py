import sys


def check_board(bb):
    check = list('WBWBWBWB')
    check_sum = 0
    for b in bb:
        check_sum += sum([ord(a) ^ ord(b) for a, b in zip(b, check)])//21
        check.reverse()
    return check_sum if check_sum < 32 else 64 - check_sum


R, C = map(int, sys.stdin.readline().split())

board = []

for i in range(R):
    line = sys.stdin.readline()
    board.append(line if line[-1] != '\n' else line[:-1])

min_sum = 999999
for r in range(0, R-7, 1):
    for c in range(0, C-7, 1):
        min_sum = min(check_board([line[c:c+8] for line in board[r:r+8]]), min_sum)


print(min_sum)

