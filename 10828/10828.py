import sys

count = int(sys.stdin.readline())

stack = []
for _ in range(count):
    data = sys.stdin.readline().split()
    if data[0] == 'push':
        stack.append(int(data[1]))
    elif data[0] == 'pop':
        if len(stack) > 0:
            num = stack.pop()
        else:
            num = -1
        print(num)
    elif data[0] == 'size':
        print(len(stack))
    elif data[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif data[0] == 'top':
        print(stack[-1] if len(stack) > 0 else -1)





