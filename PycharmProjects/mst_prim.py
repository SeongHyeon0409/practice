
from collections import defaultdict
import heapq

n = int(input())
#INF = 9999999

for i in range(n):

    edge = int(input())
    edges = []

    for j in range(edge):
        num = list(map(int, input().strip().split(" ")))
        a = num[0]
        b = num[2:]
        for l in range(0, num[1]):
            c = b[2*l] # 0 2 4
            d = b[2*l+1] # 1 3 5
            edges.append((str(a), str(c), d))

    minimum_spanning_tree = []
    adjacent_edges = defaultdict(list)

    for node1, node2, weight in edges:
        adjacent_edges[node1].append((weight, node1, node2))
        adjacent_edges[node2].append((weight, node2, node1))

    connected = set('1')
    candidated_edge = adjacent_edges['1']

    heapq.heapify(candidated_edge)

    while candidated_edge:
        weight, node1, node2= heapq.heappop(candidated_edge)

        if len(candidated_edge) > edge:
            break

        if node2 not in connected:
            connected.add(node2)
            minimum_spanning_tree.append((node1, node2, weight))

            for edge1 in adjacent_edges[node2]:
                if edge1[2] not in connected:
                    heapq.heappush(candidated_edge, edge1)

    answer = 0
    for i in minimum_spanning_tree:
        answer += i[2]

    print (answer)



