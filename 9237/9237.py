def invitation():
    count = int(input())
    trees = list(map(int, input().split()))

    trees.sort()
    for i in range(len(trees)):
        trees[i] += i

    print(max(trees)+2)


invitation()


