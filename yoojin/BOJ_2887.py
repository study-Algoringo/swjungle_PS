import sys
read = sys.stdin.readline

# union에 포함되는지 확인하는 함수
def find_union(x):
    if x != parents[x]:
        parents[x] = find_union(parents[x])
    return parents[x]

n = int(read())
xlst = []; ylst = []; zlst = []
distances = []
parents = [x for x in range(n + 1)]

for i in range(n):
    x, y, z = map(int, read().split())
    xlst.append((x, i))
    ylst.append((y, i))
    zlst.append((z, i))
xlst.sort(); ylst.sort(); zlst.sort()

for curList in xlst, ylst, zlst:
    for i in range(1, n):
        w1, a = curList[i-1]
        w2, b = curList[i]
        distances.append((abs(w1 - w2), a, b))
distances.sort()

answer = 0; count = 0
for distance, a, b in distances:
    if find_union(a) != find_union(b):
        parents[find_union(b)] = find_union(a)
        answer += distance
        count += 1

        if count >= n - 1:
            break

print(answer)