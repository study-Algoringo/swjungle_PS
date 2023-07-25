import sys
from collections import deque
read = sys.stdin.readline

# snake - 덱으로 가장 앞에는 머리, 가장 끝은 꼬리
snake = deque([[1, 1]])
mark = deque([])
# direction - 이차원 배열, 초와 방향을 지정
direction = deque([])

N = int(read())
apple = int(read())
for _ in range(apple):
    i = list(map(int, read().split()))
    mark.append(i)
    
L = int(read())
for _ in range(L):
    direction_list = list(read().split())
    direction.append(direction_list)

# 종료 조건 - snake 머리(덱 가장 앞)가 벽이나 몸에 닿을 경우
cnt = 0
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
order = 1
while 0 < snake[0][0] <= N and 0 < snake[0][1] <= N:
    # 이동 시 방향이 바뀌지 않으면 그대로, 방향이 바뀌면 [dx, dy]를 바꾸기
    next_head = [0, 0]
    if direction and int(direction[0][0]) == cnt:
        if direction[0][1] == 'D':
            order  += 1
        else:
            order -= 1
        direction.popleft()
    order = order % 4
    next_head[0] = snake[0][0] + d[order][0]
    next_head[1] = snake[0][1] + d[order][1]
    cnt += 1
    if next_head in snake:
        break
    # 사과 처리
    if next_head not in mark:
        snake.pop()
    else:
        mark.remove(next_head)
    snake.appendleft(next_head)
print(cnt)