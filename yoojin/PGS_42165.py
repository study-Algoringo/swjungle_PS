from collections import deque
def dfs(cnt, value, num, target, numbers):
    ret = 0
    if cnt == len(numbers):
        if value == target:
            return 1
        return 0
    
    ret += dfs(cnt + 1, value - numbers[cnt], num, target, numbers)
    ret += dfs(cnt + 1, value + numbers[cnt], num, target, numbers)
    return ret

def solution(numbers, target):
    answer = dfs(0, 0, 0, target, numbers)
        
    return answer