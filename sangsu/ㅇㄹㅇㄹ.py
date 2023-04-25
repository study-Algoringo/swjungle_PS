import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a,b,c = map(int, input().split())
    cnt = 0
    if a>= 10:
        cnt += 1
    if b >=10:
        cnt += 1
    if c >=10:
        cnt += 1
        
    if cnt ==0:
        print("")