import sys
read = sys.stdin.readline

slide_list = []
max_width = 0; max_height = 0
k = int(read())
for i in range(6):
    a, b = map(int, read().split())
    slide_list.append(b)
    if a == 1 or a == 2 :
        if b > max_width:
            max_width = b
            w_idx = i
    else:
        if b > max_height:
            max_height = b
            h_idx = i

# 가장 긴 가로 길이와 가장 긴 세로 길이의 곱이 전체 넓이
big_square = max_width * max_height

# 최장 가로 길이의 양 옆 변의 차이 -> 뺄 사각형의 가로
small_height = abs(slide_list[(w_idx - 1)%6] - slide_list[(w_idx + 1)%6])
# 최장 세로 길이의 양 옆 변의 차이 -> 뺄 사각형의 세로
small_width = abs(slide_list[(h_idx - 1)%6] - slide_list[(h_idx + 1)%6])

print((big_square - small_height * small_width) * k)