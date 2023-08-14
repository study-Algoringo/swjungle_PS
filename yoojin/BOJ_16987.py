import sys
from itertools import permutations
read = sys.stdin.readline

eggs = []
answer = 0
n = int(read())

for _ in range(n):
    eggs.append(list(map(int, read().split())))

def dfs(start):
    global answer
    # 계란을 리스트에 있는 순서대로 치면서, 현재 남은 계란 + 깨진 계란의 횟수가 최댓값보다 작으면 return
    # 처음 든 계란으로 어떤 계란을 깨야 할지??
    if start == n:
        total = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                total += 1
        answer = max(answer, total)
        return
    
    # 쥐고 있던 계란이 이미 깨진 경우
    if eggs[start][0] <= 0:
        dfs(start + 1)
        return
    
    check = True
    for i in range(n):
        if i == start:
            continue
        if eggs[i][0] > 0:
            check = False
            break

    # 다 깨져있는 경우 (더이상 깰 계란이 없는 경우)
    if check:
        answer = max(answer, n - 1)
        return
    
    for i in range(n):
        if i == start or eggs[i][0] <= 0:
            continue
        eggs[start][0] -= eggs[i][1]
        eggs[i][0] -= eggs[start][1]
        dfs(start + 1)
        eggs[start][0] += eggs[i][1]
        eggs[i][0] += eggs[start][1]

dfs(0)
print(answer)