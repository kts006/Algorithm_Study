count = int(input())

for _ in range(count):
    datas = list(input())
    stack = []
    while datas:
        data = datas.pop(0)
        if data == '(':
            stack.append(data)

        elif data == ')':
            if len(stack) == 0:
                stack.append(data)
                break
            stack.pop()
    # print(stack)
    print('YES' if not stack else 'NO')
