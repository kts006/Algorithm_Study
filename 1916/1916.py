import heapq

node_count = int(input())
edge_count = int(input())

edges = {}

for _ in range(edge_count):
    s, e, w = map(int, input().split())
    if s not in edges.keys():
        edges[s] = {}
    if e in edges[s].keys():
        w = min([edges[s][e], w])
    edges[s][e] = w

start, end = map(int, input().split())

dist = {node: 100000 for node in edges}
dist[start] = 0
queue = []
heapq.heappush(queue, [dist[start], start])

while queue:
    cur_dist, cur_node = heapq.heappop(queue)
    if dist[cur_node] < cur_dist:
        continue

    for next_node, weight in edges[cur_node].items():
        distance = cur_dist + weight

        if distance < dist[next_node]:
            dist[next_node] = distance
            heapq.heappush(queue, [distance, next_node])z
