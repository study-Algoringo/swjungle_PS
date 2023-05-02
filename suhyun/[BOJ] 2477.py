import sys
N = int(sys.stdin.readline())
solution = []
width = []
length = []

for _ in range(6):
    n,l = map(int,sys.stdin.readline().split())
    solution.append([n,l])
    if n == 3 or n==4:
        width.append(l)
    else:
        length.append(l)

result = []
for i in range(6):
    if solution[i][0] == solution[(i+2)%6][0]:
        result.append(solution[(i+1)%6][1])

print((max(length)*max(width) - result[0]*result[1])*N)