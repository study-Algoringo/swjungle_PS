'''
# 시간초과
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

time = list(map(int, input().split()))
rec = []

nm = n // m
cnt = 1

old_max = int(1e9)
maxi = 0
bp = 0

if m == 1:
    print(sum(time))
    exit()

for i in range(1, len(time) + 1):
    if i % nm == 0:
        rec.append(time[i - nm:i])
        cnt += 1
    if cnt == m:
        rec.append(time[i:])
        break
if n == m:
    print(max(rec)[0])
    exit()

while True:
    new_max = 0

    for j in range(len(rec)):
        if sum(rec[j]) > new_max:
            new_max = sum(rec[j])
            maxi = j

    if maxi != 0:
        rec[maxi-1] = rec[maxi-1] + [rec[maxi][0]]
        rec[maxi] = rec[maxi][1:]
    else:
        rec[maxi+1] = [rec[maxi][-1]] + rec[maxi+1]
        rec[maxi] = rec[maxi][:-1]
        bp += 1

    if old_max > new_max:
        old_max = new_max
    if bp == 2:
        print(old_max)
        break
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

time = list(map(int, input().split()))

left = max(time)  
right = sum(time)  

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    curr_sum = 0
    max_sum = 0

    for t in time:
        curr_sum += t
        if curr_sum > mid:
            cnt += 1
            curr_sum = t
        max_sum = max(max_sum, curr_sum)

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)
