import sys
input = sys.stdin.readline
n = int(input())
planets = []
for i in range(n):
    edges = list(map(int, input().split()))
    for j in range(n):
        if i != j:
            planets.append((edges[j], i+1, j+1))
        
planets.sort()
    
parent = {}
rank = {}
answer = 0

def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
        
    return parent[node]

def union(node_u, node_v):
    root1 = find(node_u)
    root2 = find(node_v)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
            
for i in range(1, n+1):
    parent[i] = i
    rank[i] = 0
    

for planet in planets:
    a,b,c = planet
    if find(b) != find(c):
        union(b,c)
        answer += a
        
print(answer)