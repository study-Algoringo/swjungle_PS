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