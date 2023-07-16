import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
indegree = [0]*(n+1)
subject_list = [[] for _ in range(n+1)]
semester = [0] *(n+1)
for i in range(m):
    a,b = map(int, input().split())
    subject_list[a].append(b)
    indegree[b] += 1
que = deque([])
for i in range(1, n+1):
    if not indegree[i]:
        que.append(i)
        semester[i] = 1
while que:
    a = que.popleft()
    for subject in subject_list[a]:
        semester[subject] = max(semester[subject], semester[a]+1)
        indegree[subject] -= 1
        if not indegree[subject]:
            que.append(subject)
            
semester.remove(0)
semester = map(str, semester)
print(" ".join(semester))