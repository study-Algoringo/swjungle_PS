# BFS
# import sys
# from collections import deque
# N = int(sys.stdin.readline())
# idx = 0

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# while N!=0:
#     idx+=1
#     que = deque([[0,0]])
#     arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
#     theif = [[99999 for _ in range(N)] for _ in range(N)] 
#     theif[0][0] = arr[0][0]

#     while que:
#         x,y = que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0<=nx<N and 0<=ny<N:
#                  if theif[nx][ny] > theif[x][y] + arr[nx][ny]:
#                     theif[nx][ny] = theif[x][y] + arr[nx][ny]
#                     que.append([nx,ny])

#     print("Problem {0}: {1}".format(idx,theif[N-1][N-1]))
#     N = int(sys.stdin.readline())

# 다익스트라

# import heapq
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dijkstra():
#     q = []
#     heapq.heappush(q, (graph[0][0], 0, 0))
#     distance[0][0] = 0

#     while q:
#         cost, x, y = heapq.heappop(q)

#         if x == n - 1 and y == n - 1:
#             print(f'Problem {count}: {distance[x][y]}')
#             break


#         for i in range(4):
#             new_x = x + dx[i]
#             new_y = y + dy[i]

#             if 0 <= new_x < n and 0 <= new_y < n:
#                 distance[new_x][new_y] = min(distance[new_x][new_y], cost + graph[new_x][new_y])
#                 heapq.heappush(q, (cost + graph[new_x][new_y], new_x, new_y))

# count = 1

# while True:
#     n = int(input())
#     if n == 0:
#         break

#     graph = [list(map(int, input().split())) for _ in range(n)]
#     distance = [[INF] * n for _ in range(n)]

#     dijkstra()
#     count += 1

# 다익스트라

import sys
import heapq
def dkjstra(N):
    result = [[int(1e9)]*N for _ in range(N)]
    hque = [[arr[0][0],0,0]]
    result[0][0] = arr[0][0]

    while hque:
        data,x,y = heapq.heappop(hque)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<N:
                if result[nx][ny] > arr[nx][ny] + result[x][y]:
                    result[nx][ny] = arr[nx][ny] + result[x][y]
                    heapq.heappush(hque,[result[nx][ny], nx, ny])

    return result[N-1][N-1]
        
idx = 0
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    idx +=1
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    print(f"Problem {idx}: {dkjstra(N)}")
