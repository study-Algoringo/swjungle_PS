from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque([])
    
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        i = i.lower()
        if i in q:
            q.remove(i)
            q.append(i)
            answer += 1
        elif i not in q and len(q) < cacheSize:
            q.append(i)
            answer += 5
        else:
            q.popleft()
            q.append(i)
            answer += 5
            
    return answer
