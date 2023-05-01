import sys
input = sys.stdin.readline
melon = []
garo = []
sero = []
east = 0
west = 0
south = 0
north = 0
k = int(input())
for i in range(6):
    a,b = map(int, input().split())
    
    melon.append([a,b])
    if a == 1:
        east += 1
        garo.append(b)
    if a == 2:
        west += 1
        garo.append(b)
    if a == 3:
        south += 1
        sero.append(b)
    if  a== 4:
        north += 1
        sero.append(b)
if east == 2 and south == 2:
    order = (1,3)
elif west == 2 and south == 2:
    order = (2,3)
elif east == 2 and north == 2:
    order = (1,4)
elif west == 2 and north == 2:
    order = (2,4)

for i in range(6):
    if (melon[i-1][0], melon[i][0]) == order:
        minus = melon[i-1][1] * melon[i][1]
        
total = max(garo) *max(sero)

print((total - minus)*k) 