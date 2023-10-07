import sys
read = sys.stdin.readline

# 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야
# 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같

n, l, r, x = map(int, read().split())
difficulty = list(map(int, read().split()))

