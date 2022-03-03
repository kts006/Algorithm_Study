
save_dict = {}

def fib(n):
    if n in save_dict.keys():
        return save_dict[n]
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        count = tuple(x+y for x, y in zip(fib(n - 1), fib(n - 2)))
        save_dict[n] = count
        return count


case = int(input())
for _ in range(case):
    num = int(input())
    print(*fib(num))
