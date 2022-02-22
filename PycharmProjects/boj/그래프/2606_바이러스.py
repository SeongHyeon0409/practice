n = int(input()) # number of computers 1 ~ 100
t = int(input()) # number of twins

edges = dict()

for i in range(1, n+1):
    edges[i] = []

for i in range(t):
    s ,e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

visited, non_visited = list(), list()

non_visited.append(1)

while non_visited:
    node = non_visited.pop()
    if node not in visited:
        visited.append(node)
        non_visited.extend(edges[node])

print(len(visited)-1)
