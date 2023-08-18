import sys
read = sys.stdin.readline

n = int(read())
result = list(map(int, read().split()))
cards = [i for i in range(1, n + 1)]

# (2, k) 카드 섞기
def mix(cards, k):
    if k < 0:
        return cards
    
    length = len(cards); pos = 2 ** k
    cards = cards[length - pos:] + cards[:length - pos]
    cards[:pos] = mix(cards[:pos], k - 1)
    return cards
    
for i in range(1, 10):
    for j in range(1, 10):
        if mix(mix(cards, i), j) == result:
            print(i, j)
            sys.exit()