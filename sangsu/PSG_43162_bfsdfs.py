# from collections import deque

# def solution(n, computers):
#     visited = [0]*n
#     queue = deque()
#     answer = 0
#     for i in range(n):
#         if visited[i]:
#             continue
#         else:
#             queue.append(i)
#             visited[i] = 1
#             answer += 1
#             while queue:
#                 comp = queue.popleft()
#                 for j, net_comp in enumerate(computers[comp]):
#                     if not visited[j] and net_comp:
#                         queue.append(j)
#                         visited[j] = 1
#     return answer


# dfs 풀이

def solution(n, computers):
    answer =0
    visited = [0]*n
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer += 1
            
    return answer

def dfs(node, visited, computers):
    visited[node] = 1
    for next_node, connect in enumerate(computers[node]):
        if not visited[next_node] and connect:
            dfs(next_node, visited, computers)
    return
        





