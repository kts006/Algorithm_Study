import copy


def get_tree():
    node_count, edge_count = map(int, input().split(' '))

    graph = []
    for _ in range(edge_count):
        start_node, end_node, weight = map(int, input().split(' '))
        graph.append((start_node, end_node, weight))

    graph.sort(key=lambda e: e[2])
    edge = graph.pop(0)
    min_tree = [edge]
    node_set = set()
    node_set.add(edge[0])
    node_set.add(edge[1])

    while graph:
        loop_graph = copy.deepcopy(graph)
        for e in loop_graph:
            if (e[0] in node_set) ^ (e[1] in node_set):
                graph.remove(e)
                min_tree.append(e)
                node_set.add(e[0])
                node_set.add(e[1])
                break
            elif e[0] in node_set and e[1] in node_set:
                graph.remove(e)

    return sum([edge[2] for edge in min_tree])


min_weight = get_tree()
print(f"\n {min_weight}")
