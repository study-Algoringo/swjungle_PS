from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque([])
    queue.append(begin)
    visited = {}
    
    for word in words:
        visited[word] = 0
    visited[begin] = 0
    
    while queue:
        current = queue.popleft()
        if current == target:
            return visited[current]
        for word in words:
            temp_cnt = 0
            if not visited[word]:
                for j in range(len(word)):
                    if word[j] != current[j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    queue.append(word)
                    visited[word] = visited[current] + 1
    
    return answer