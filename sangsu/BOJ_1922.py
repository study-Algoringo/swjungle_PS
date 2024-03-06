import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = {}
rank = {}
edges = []
answer = 0
for i in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
    
edges.sort()

def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
        
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
        
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
            
for i in range(1, n+1):
    parent[i] = i
    rank[i] = 0
    
for edge in edges:
    x,y,z = edge
    if find(y) != find(z):
        union(y,z)
        answer += x
    
        
print(answer)
    
