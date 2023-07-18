import sys
input = sys.stdin.readline

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
        
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

n,m = int(input()),int(input())
edge = []
parents = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))
edge.sort(reverse = True)

r,cnt = 0,0
while cnt != n-1:
    w,a,b = edge.pop()
    if find(a) == find(b):
        continue
    
    union(a,b)
    r += w
    cnt += 1
print(r)
