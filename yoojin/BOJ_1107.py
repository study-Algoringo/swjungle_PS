import sys
read = sys.stdin.readline

num = read().strip()
m = int(read())
buttons = list(read().split())

# num에 가장 가까운 번호 구하기
for i, n in enumerate(num):
    if n not in buttons: