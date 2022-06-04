
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find_set(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_set(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find_set(vertice1)
    root2 = find_set(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


n = int(input())

for i in range(n):
    parent = dict()
    rank = dict()

    edge = int(input())
    edges = []

    for k in range(1, edge+1):
        make_set(k)

    for j in range(edge):
        num = list(map(int, input().strip().split(" ")))
        a = num[0]
        b = num[2:]
        for l in range(0, num[1]):
            c = b[2*l] # 0 2 4
            d = b[2*l+1] # 1 3 5
            edges.append((a, c, d))

    edges.sort(key=lambda x: x[2])
    minimum_spanning_tree = []

    for edge in edges:
        vertice1, vertice2, weight = edge
        if find_set(vertice1) != find_set(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)

    answer = 0
    for i in minimum_spanning_tree:
        answer += i[2]

    print (answer)



