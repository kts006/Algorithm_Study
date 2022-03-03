import sys

N, K = map(int, sys.stdin.readline().split())
stuff = [0]
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    stuff.append((W, V))

knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(1, K+1):
        if w >= stuff[i][0]:
            knapsack[i][w] = max(knapsack[i-1][w - stuff[i][0]] + stuff[i][1], knapsack[i-1][w])
        else:
            knapsack[i][w] = knapsack[i-1][w]

print(knapsack[N][K])

