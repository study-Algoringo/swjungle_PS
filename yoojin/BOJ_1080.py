import sys

A = []; B = []; count = 0
n, m = map(int, input().split())
# (i, j)를 확인한 후 A와 B 행렬의 값이 다르면 바꾸기

for _ in range(n):
    A.append(list(map(int, list(input()))))
for _ in range(n):
    B.append(list(map(int, list(input()))))

def flip(x, y):
    for i in range(3):
        for j in range(3):
            A[x + i][y + j] = (A[x + i][y + j] + 1) % 2

if (n < 3 or m < 3) and A != B:
    count = -1
else:
    for i in range(n - 2):
        for j in range(m - 2):
            if A[i][j] != B[i][j]:
                # (i, j)를 시작점으로 3x3 행렬의 숫자 바꾸기
                count += 1
                flip(i, j)

if A != B:
    count = -1
print(count)