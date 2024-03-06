import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
visited = [[-1] * (n + 1) for _ in range(n + 1)]

que = deque([(1, 0)])
visited[1][0] = 0

while que:
    s, c = que.popleft()

    # 화면 이모티콘을 클립보드에 복사하는 경우
    if visited[s][s] == -1:
        visited[s][s] = visited[s][c] + 1
        que.append((s, s))

    # 클립보드에 있는 이모티콘을 화면에 붙여넣기하는 경우
    if s + c <= n and visited[s + c][c] == -1:
        visited[s + c][c] = visited[s][c] + 1
        que.append((s + c, c))

    # 화면에 있는 이모티콘을 삭제하는 경우
    if s - 1 >= 0 and visited[s - 1][c] == -1:
        visited[s - 1][c] = visited[s][c] + 1
        que.append((s - 1, c))

answer = float('inf')
for i in range(n + 1):
    if visited[n][i] != -1:
        answer = min(answer, visited[n][i])

print(answer)


    
    
    
#기존에는 스크린에 떠있는 이모티콘 수에 따라서만 방문 처리를 해줬었음.. 화면에 같은 이모티콘 수가 있어도 클립보드에 있는 이모티콘의 개수는 다를 수 있으므로 2차원 배열로 방문처리를 해줘야함
    
    # import sys
# input = sys.stdin.readline
# from collections import deque

# n = int(input())
# visited = [99999] *2000

# visited[0] = 0
# screen = 1
# board = 0

# que = deque([(1,0,0,0)])
# while que:
#     a,b,c,d = que.popleft()
#     if visited[a] == 99999 and d ==0:
#         visited[a] = c
#         temp1 = (a-1, b, c+1,0)
#         temp2 = (a+b, b, c+1,0)
#         temp3 = (a, a, c+1,1)
        
#         if visited[a-1] == 99999 and a-1> 0:
#             que.append(temp1)
        
#         if a+b <2000:
#             if visited[a+b] == 99999:
#                 que.append(temp2)
            
#         que.append(temp3)
        
#     elif d == 1:
#         temp1 = (a-1, b, c+1,0)
#         temp2 = (a+b, b, c+1,0)
#         if visited[a-1] == 99999 and a-1> 0:
#             que.append(temp1)
            
#         if a+b <2000:
#             if visited[a+b] == 99999:
#                 que.append(temp2)
            
# print(visited[n])
    