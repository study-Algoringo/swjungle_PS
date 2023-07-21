import sys
read = sys.stdin.readline

t = int(read())
if t % 10 != 0:
    print(-1)
else:
    print(t // 300, (t % 300) // 60, (t % 60) // 10)