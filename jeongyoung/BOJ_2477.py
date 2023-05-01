# (가장 큰 사각형 - 제일 작은 사각형) * k
# 동서남북 = 동서(1,2), 남북(3,4)이 짝
k = int(input())
a = [list(map(int, input().split())) for _ in range(6)]
w = []
h = []
result = 0

for i in range(6):
    if a[i][0] == 1 or a[i][0] == 2:
        w.append(a[i][1])
    else:
        h.append(a[i][1])
    # print(w, h)
w.sort()
h.sort()
# print(abs(((w[0] * h[0]) - (w[2] * h[2]))* k))
print((max(w) * max(h) - min(w) * min(h))*k)
