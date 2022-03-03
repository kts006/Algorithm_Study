a, b, c = map(int, input().split())

bin_a = bin(a)[2:]
bin_b = bin(b)[2:]

if len(bin_a) > len(bin_b):
    bin_b = bin_b.zfill(len(bin_a))
else:
    bin_a = bin_a.zfill(len(bin_b))

result = ''
for a, b in zip(bin_a, bin_b):
    if b == '0':
        result += a
    elif a == b:
        result += '1' if c % 2 == 0 else '0'
    elif a != b:
        result += '0' if c % 2 == 0 else '1'

print(int(result, 2))
