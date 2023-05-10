# 시간초과나는 코드입니다... 도와주세요

import sys
input = sys.stdin.readline

n, h = map(int, input().split())
bug = [0]*h
for i in range(n):
    l = int(input())
    if i%2 == 0:
        for j in range(l):
            bug[j] += 1
            
    if i%2 == 1:
        for j in range(l):
            bug[h -j-1] += 1
            
low = min(bug)
cnt = bug.count(low)

print(low,cnt)

