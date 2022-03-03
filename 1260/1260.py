import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    graph[S][E] = 1
    graph[E][S] = 1


def bfs(start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        for i in range(len(graph[start])):
            if graph[node][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)
    print(*visited)


def dfs(start, visited=list()):
    visited.append(start)
    print(start, end=' ')
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and i not in visited:
            dfs(i, visited)


dfs(V)
print()
bfs(V)








