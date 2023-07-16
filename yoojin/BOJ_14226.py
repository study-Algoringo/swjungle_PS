from collections import deque

def bfs(target):
    # 현재 이모티콘 개수, 클립보드 이모티콘 개수, 시간
    queue = deque([(1, 0, 0)])
    visited = set([(1, 0)])

    while queue:
        curr, clip, time = queue.popleft()

        if curr == target:
            return time
        
        if (curr, curr) not in visited:
            queue.append((curr, curr, time + 1))
            visited.add((curr, curr))

        if curr + clip <= target and (curr + clip, clip) not in visited:
            queue.append((curr + clip, clip, time + 1))
            visited.add((curr + clip, clip))
        
        if curr - 1 >= 0 and (curr - 1, clip) not in visited:
            queue.append((curr - 1, clip, time + 1))
            visited.add((curr - 1, clip))

    return -1

target = int(input())
answer = bfs(target)
print(answer)
