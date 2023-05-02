import sys
input = sys.stdin.readline

a,b = map(int, input().split())
n = int(input())
stores = []
for i in range(n):
    x, y = map(int, input().split())
    stores. append([x,y])
    
p, q = map(int, input().split())
s = 0
if p == 1:
    for store in stores:
        if store[0] == 2:
            s += min(b+q+store[1], 2*a+b-q-store[1])
        elif store[0] ==3:
            s += q+store[1]
        elif store[0] == 4:
            s += a-q +store[1]
        else :
            s += abs(store[1]-q)
            
if p == 2:
    for store in stores:
        if store[0] == 1:
            s += min(b+q+store[1], 2*a+b-q-store[1])
        elif store[0] ==3:
            s += q+b-store[1]
        elif store[0] == 4:
            s += a-q +b-store[1]
        else :
            s += abs(store[1]-q)
if p == 3:
    for store in stores:
        if store[0] == 4:
            s += min(a+q+store[1], a+2*b-q-store[1])
        elif store[0] ==1:
            s += q+store[1]
        elif store[0] == 2:
            s += b-q +store[1]
        else :
            s += abs(store[1]-q)
            
if p == 4:
    for store in stores:
        if store[0] == 3:
            s += min(a+q+store[1], a+2*b-q-store[1])
        elif store[0] ==1:
            s += q+a-store[1]
        elif store[0] == 2:
            s += b-q +a-store[1]
        else :
            s += abs(store[1]-q)
            
print(s)
