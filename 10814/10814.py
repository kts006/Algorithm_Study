count = int(input())

member_list = []
for _ in range(count):
    age, name = input().split()
    member_list.append((int(age), name))

member_list.sort(key=lambda x:x[0])
for age, name in member_list:
    print(age, name)