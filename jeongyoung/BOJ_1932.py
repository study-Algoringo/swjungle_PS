# 정수 삼각형 1932
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# print(data)

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            data[i][0] += data[i-1][0]
        elif j == i:
            data[i][j] += data[i-1][j-1]
        else:
            data[i][j] += max(data[i-1][j-1], data[i-1][j])

print(max(data[n-1]))
