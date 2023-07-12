import sys
from itertools import combinations

read = sys.stdin.readline

# word -> 26짜리 bit로 바꿈
def word2bit(word):
    bit = 0
    for i in word:
        bit = bit | 1 << ord(i) - ord('a')
    return bit

# 주어진 word 배열 받기
n, k = map(int, read().split())
words = [read().rstrip() for _ in range(n)]

if k < 5:
    print(0)
else:
    answer = 0
    bits = list(map(word2bit, words))
    base_bit = word2bit('antic')

    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    # antic 제외 (비트)알파벳들 중 k-5개 뽑기
    for combination in combinations(alphabet, k-5):
        # 알파벳과 antic을 모두 합친, 내가 알고 있는 알파벳들의 조합(을 비트로 바꾼 것)
        know_bit = sum(combination) | base_bit
        count = 0
        for bit in bits:
            # 만약 know_bit가 가지고 있는 조합이 bit를 포함/bit와 같은 경우
            if know_bit & bit == bit:
                count += 1
        answer = max(count, answer)
    print(answer)
