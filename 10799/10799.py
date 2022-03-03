datas = list(input())

result = 0
panel = 0
piece = 0
stack = []
for data in datas:
    if data == '(':
        panel += 1
        stack.append(data)

    elif data == ')':
        panel -= 1
        piece += 1
        stack.pop()
    if not stack:
        result += piece * panel
        panel = 0
        piece = 0

print(result)

