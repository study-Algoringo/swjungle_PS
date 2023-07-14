import sys
read = sys.stdin.readline

# 길이를 기준으로 이분 탐색
# 최소 길이 - 가장 긴 길이의 랜선을 n으로 나눈 값
# 최대 길이 - 랜선 중 가장 짧은 길이

def count_lan_cables(nums, length):
    count = 0
    for num in nums:
        count += num // length
    return count

def binary_search(nums, n):
    start = 1; end = max(nums)
    while start <= end:
        middle = (start + end) // 2
        count = count_lan_cables(nums, middle)
        if count >= n:
            start = middle + 1
        else:
            end = middle - 1
    return end

k, n = map(int, read().split())
nums = []
for i in range(k):
    nums.append(int(read()))

answer = binary_search(nums, n)
print(answer)