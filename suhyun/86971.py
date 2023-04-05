import sys
def bfs(x,n,bot):
    que = []
    que.append(x)
    visited = [False]*(n+1)
    cnt=1
    visited[x]=True
    while que:
        temp = que.pop(0)
        for i in bot[temp]:
            if not visited[i]:
                visited[i] = True
                cnt+=1
                que.append(i)
    return cnt

def solution(n, wires):
    answer = sys.maxsize
    bot = [[] for _ in range(n+1)]
    for a,b in wires:
        bot[a].append(b)
        bot[b].append(a)


    answer = n
    # 끝는 방법 
    for a,b in wires:
        bot[a].remove(b)
        bot[b].remove(a)

        answer=min(answer,abs(bfs(a,n,bot)-bfs(b,n,bot)))

        bot[a].append(b)
        bot[b].append(a)

    return answer


wire = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

print(solution(9,wire))