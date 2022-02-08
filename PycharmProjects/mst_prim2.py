from heapdict import heapdict

n = int(input())
INF = 9999999

for i in range(n):

    edge = int(input())
    graph = dict()

    for j in range(edge):
        num = list(map(int, input().strip().split(" ")))
        a = num[0]
        b = num[2:]

        edges = dict()
        for l in range(0, num[1]):
            c = b[2*l] # 0 2 4
            d = b[2*l+1] # 1 3 5
            edges[str(c)] = d

        graph[str(j+1)] = edges


    minimum_spanning_tree = []
    keys = heapdict()
    previous = dict()
    first = '1'
    total_weight = 0

    for node in graph.keys():
        keys[node] = INF
        previous[node] = None

    keys[first], previous[first] = 0, first
    print(keys)

    while keys:
        current_node, current_key = keys.popitem()
        minimum_spanning_tree.append([previous[current_node], current_node, current_key])
        total_weight += current_key
        for adjacent, weight in graph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                previous[adjacent] = current_node

    print (total_weight)



