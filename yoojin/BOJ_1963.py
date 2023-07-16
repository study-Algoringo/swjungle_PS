import sys
from collections import deque
import math

read = sys.stdin.readline

prime_number = []
array = [True for i in range(10000)]

# 2보다 크고 i의 제곱근보다 작은 수들에 대해
for i in range(2, int(math.sqrt(10000)) + 1):
    if array[i] == True:
        for j in range(i * i, 10000, i):
            array[j] = False

# enumerate 이용, prime이 True이면 index를 이용해 prime 가져옴
prime_number = [num for num, prime in enumerate(array) if prime and num >= 1000]

def minimum_convert(start, end):
    if start == end:
        return 0
    
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    # start보다 크고 end보다 작은 & visited 하지 않은 소수 & 한 자리만 바꾸기
    
    while queue:
        current, num = queue.popleft()
        
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue

                new_num = int(str(current)[:i] + str(j) + str(current)[i+1:])

                if new_num == end:
                    return num + 1
                if new_num in prime_number and new_num not in visited:
                    queue.append((new_num, num + 1))
                    visited.add(new_num)
    return -1

t = int(read())
for i in range(t):
    start, end = map(int, read().split())
    print(minimum_convert(start, end))