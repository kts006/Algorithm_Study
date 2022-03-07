import sys

count = int(sys.stdin.readline())
num_list = []
num_dict = dict()
for _ in range(count):
    num = int(sys.stdin.readline())
    num_list.append(num)
    num_dict[num] = num_dict[num] + 1 if num in num_dict.keys() else 1

num_list.sort()
sorted_dict = sorted(num_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)
print(round(sum(num_list) / count))
print(num_list[count // 2])
new_list = [key[0] for key in sorted_dict if key[1] == sorted_dict[0][1]]
print(new_list[-2 if len(new_list) > 1 else -1])
print(num_list[-1] - num_list[0])
