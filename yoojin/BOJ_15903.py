import sys
import heapq
read = sys.stdin.readline

n, m = map(int, read().split())
cards = list(map(int, read().split()))
heapq.heapify(cards)

for i in range(m):
    # 매 시도마다 가장 작은 두 개를 더하기
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    heapq.heappush(cards, a + b)
    heapq.heappush(cards, a + b)

print(sum(cards))