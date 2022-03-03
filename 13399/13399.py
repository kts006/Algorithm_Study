def get_min():
    count = input()
    peoples = list(map(int, input().split()))
    peoples.sort()
    min_times = sum([sum(peoples[:i+1]) for i in range(len(peoples))])
    print(min_times)


get_min()
