import sys

N = int(sys.stdin.readline())
blocks = []

# 입력 및 정렬 진행
for _ in range(N):
    blocks.append(list(map(int, sys.stdin.readline().split())))
blocks.sort()

# 가장 높은 기둥의 인덱스 구하기
max_height_idx = 0
max_height = 0
for i in range(N):
    if max_height < blocks[i][1]:
        max_height = blocks[i][1]
        max_height_idx = i

# 왼쪽에서부터 가장 높은 기둥까지의 면적 구하기
total_area = 0
left_height = 0
for i in range(max_height_idx):
    if blocks[i][1] > left_height:
        left_height = blocks[i][1]
    total_area += left_height * (blocks[i + 1][0] - blocks[i][0])

# 오른쪽에서부터 가장 높은 기둥까지의 면적 구하기
right_height = 0
for i in range(N - 1, max_height_idx, -1):
    if blocks[i][1] > right_height:
        right_height = blocks[i][1]
    total_area += right_height * (blocks[i][0] - blocks[i - 1][0])

# 가장 높은 기둥의 면적 더하기
total_area += max_height

print(total_area)
