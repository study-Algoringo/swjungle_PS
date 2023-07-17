import sys
read = sys.stdin.readline

n = int(read())
m = int(read())
graph = []; cost = 0

for i in range(m):
    a, b, cost = map(int, read().split())
    graph.append((a, b, cost))

graph.sort(key=lambda x: x[-1])

parents = [x for x in range(n + 1)]
distance = 0; count = 0

def find_set(a):
    while a != parents[a]:
        a = parents[a]
    return a

# cycle을 만들지 않는 경우 추가
for a, b, cost in graph:
    if find_set(a) != find_set(b):
        parents[find_set(b)] = find_set(a)
        distance += cost
        count += 1

        if count >= n - 1:
            break

print(distance)