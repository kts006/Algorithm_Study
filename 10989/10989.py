import sys

count = int(sys.stdin.readline())
num_list = [0] * 10000

for _ in range(count):
    num = int(sys.stdin.readline())
    num_list[num-1] += 1

for idx, num in enumerate(num_list):
    if num > 0:
        for _ in range(num):
            print(idx+1)

