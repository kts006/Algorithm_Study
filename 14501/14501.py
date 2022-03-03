import sys

count = int(sys.stdin.readline())

counsel = []
calc = [0 for _ in range(count+1)]

for _ in range(count):
    period, pay = map(int, sys.stdin.readline().split())
    counsel.append((period, pay))

for i in range(count-1, -1, -1):
    if i + counsel[i][0] <= count:
        calc[i] = max(counsel[i][1] + calc[i + counsel[i][0]], calc[i+1])
    else:
        calc[i] = calc[i+1]

print(max(calc))
