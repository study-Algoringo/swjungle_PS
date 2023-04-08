# 백트래킹
import sys
from collections import deque
def solution(numbers, target):
    que = [[0,0],[0,0]]
    answer = 0
    num = 0
    for i in range(len(numbers)):
        x = numbers[i]
        dx = [-x,x]
        a,b = que.pop(0)
        for j in range(2):
            while a == num:
                que.append([a+1,dx[j]+b])
                a,b = que.pop(0)
                if b == target:
                    answer+=1
        num+=1
##??
    return answer
arr = [1, 1, 1, 1, 1]
print(solution(arr,3))
