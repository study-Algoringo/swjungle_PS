# answer = 0 
# def dfs(cnt, current, visited, dungeons):
#     global answer
#     answer = max(answer,cnt)
#     for i in range(len(dungeons)):
#         if not visited[i] and current >= dungeons[i][0]:
#             visited[i] = True
#             dfs(cnt+1,current-dungeons[i][1], visited, dungeons)
#             visited[i] = False

# def solution(k, dungeons):
#     global answer
#     visited = [False] * len(dungeons)
#     dfs(0,k,visited,dungeons)
#     return answer

# print(solution(80,[[80,20],[50,40],[30,10]]))

from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    print(list(permutations(range(n))))
    for order in permutations(range(n)):
        #print(t)
        cur = k
        local_ans = 0
        for t in order:
            require, consum = dungeons[t]
            if cur >= require:
                cur -= consum
                local_ans += 1
        answer = max(answer, local_ans)


    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))