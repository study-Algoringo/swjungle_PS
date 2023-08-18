import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

# 정렬한 후
# 뒤에서부터 삼각 수열 조건을 만족하는지 확인하면서 길이 체크
nums.sort()

answer = 1
for i in range(n - 1):
    for j in range(n - 1, -1, -1):
        if j < i + 1:
            continue
        if nums[i] + nums[i + 1] > nums[j]:
            answer = max(j - i + 1, answer)
print(answer)