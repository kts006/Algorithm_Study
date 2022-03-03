import sys

count = int(sys.stdin.readline())

stack = []
for _ in range(count):
    data = int(sys.stdin.readline())

    if data != 0:
        stack.append(data)
    else:
        stack.pop()

print(sum(stack))

