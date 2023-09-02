import sys
read = sys.stdin.readline

n, s = map(int, read().split())
nums = list(map(int, read().split()))

answer = 0
def dfs(idx, sum):
    global answer

    if idx >= n:
        return
    
    sum += nums[idx]
    if sum == s:
        answer += 1
    dfs(idx + 1, sum)
    dfs(idx + 1, sum - nums[idx])

dfs(0, 0)
print(answer)