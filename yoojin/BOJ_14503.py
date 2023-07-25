import sys
read = sys.stdin.readline

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
count = 0

n, m = map(int, read().split())
r, c, d = map(int, read().split())
room = [list(map(int, read().split())) for _ in range(n)]

# 0인 경우 청소되지 않은 칸, 1인 경우 벽

def clean(x, y, d):
    global count
    # 해당 칸 청소 완료 처리
    # count 1 증가
    if room[x][y] == 0:
        room[x][y] = 2
        count += 1

    # 사방에 청소되지 않은 칸이 없는 경우 후진
    for i in range(4):
        nd = d - 1
        # 다음 좌표 구하기
        nx = x + direction[nd % 4][0]
        ny = y + direction[nd % 4][1]
        
        # 다음 좌표가 그래프상 갈 수 있는 곳인 경우
        if 0 <= nx < n and 0 <= ny < m:
            # 청소해야 되는 곳이면
            if room[nx][ny] == 0:
                clean(nx, ny, nd)
                return
        d = nd
    else:
        # 후진 좌표 구하기
        bx = x + direction[(d - 2) % 4][0]
        by = y + direction[(d - 2) % 4][1]
        if 0 <= bx < n and 0 <= by < m:
            if room[bx][by] != 1:
                clean(bx, by, d)

clean(r, c, d)
print(count)