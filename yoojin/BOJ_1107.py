import sys
read = sys.stdin.readline

num = read().strip()
m = int(read())
buttons = list(read().split())

# num에 가장 가까운 번호 구하기
for i, n in enumerate(num):
    # 해당 자리수가 
    if n not in buttons:

# 그 번호에서 -/+를 이용해서 목표 숫자 만들기