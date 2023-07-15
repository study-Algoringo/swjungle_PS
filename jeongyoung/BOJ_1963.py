#1963 소수 경로
# 소수? 에스~~체 / bfs
import collections


def bfs(num):
    q = collections.deque()
    q.append([num, 0])
    V[num] = 1
    while q:
        num, cnt = q.popleft()
        if num == dest_v:
            return cnt
        for i, n in enumerate(str(num)):
            for nn in range(10):
                if i == nn == 0:
                    continue
                elif int(n) == nn:
                    continue
                nxt_v = num + (nn - int(n)) * 10 ** (3 - i)
                if Prime[nxt_v] and not V[nxt_v]:
                    q.append([nxt_v, cnt + 1])
                    V[nxt_v] = 1
    return 'Impossible'


Prime = [0, 0] + [1] * 9998
for i in range(2, 10000):
    if Prime[i]:
        for j in range(2 * i, 10000, i):
            Prime[j] = 0

T = int(input())
for _ in range(T):
    start_v, dest_v = map(int, input().split())
    V = [0] * 10000
    print(bfs(start_v))
