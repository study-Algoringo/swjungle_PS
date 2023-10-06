import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

n = int(read())
picture = list(read().rstrip() for _ in range(n))
visited = [[0] * n for _ in range(n)]
answer1 = 0; answer2 = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# dfs를 이용해 같은 알파벳이면 같은 구역으로 판단
def dfs(x, y):
    # 방문 처리
    visited[x][y] = 1
    # 인접한 4방향 탐색, 같은 알파벳이면 go
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 방문하지 않았고, 같은 알파벳이면
            if not visited[nx][ny] and picture[x][y] == picture[nx][ny]:
                dfs(nx, ny)

def colored_dfs(x, y):
    # 방문 처리
    visited[x][y] = 1
    # 인접한 4방향 탐색, 같은 알파벳이면 go
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 방문하지 않았고, 같은 알파벳이면
            if not visited[nx][ny]:
                if picture[x][y] == picture[nx][ny]:
                    colored_dfs(nx, ny)
                elif picture[x][y] in ['R', 'G'] and picture[nx][ny] in ['R', 'G']:
                    colored_dfs(nx, ny)

def solution(function):
    global visited
    answer = 0; visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                function(i, j)
                answer += 1
    return answer

print(solution(dfs), solution(colored_dfs))