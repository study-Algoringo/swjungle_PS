import sys
read = sys.stdin.readline

s = list(read().strip())
t = list(read().strip())

# T의 마지막에 A가 있으면 제거
# T의 맨앞이 B라면 B를 제거하고 뒤집기
def dfs(t):
    if s == t:
        print(1)
        sys.exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])

dfs(t)
print(0)