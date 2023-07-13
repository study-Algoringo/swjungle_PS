import sys
read = sys.stdin.readline

n = int(read())
cards = sorted(list(map(int, read().split())))
m = int(read())
find_cards = list(map(int, read().split()))

def find_card(card, arr):
    left = 0; right = len(arr) - 1
    while left <= right:
        middle_idx = (left + right) // 2
        # 같으면 return 1
        if arr[middle_idx] == card:
            return 1
        elif arr[middle_idx] < card:
            left = middle_idx + 1
        
        else:
            right = middle_idx - 1
    return 0

for card in find_cards:
    print(find_card(card, cards))