import sys
import heapq
read = sys.stdin.readline

t = int(read())

def solution(arr):
    ret = 0
    heapq.heapify(arr)

    while len(arr) > 1:
        # 최소 값 뽑고, 두 수의 합을 다시 push
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        ret += a + b
        heapq.heappush(arr, a + b)
    return ret

for i in range(t):
    n = int(read())
    arr = list(map(int, read().split()))

    print(solution(arr))