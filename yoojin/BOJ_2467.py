import sys
read = sys.stdin.readline

n = int(read())
# 합이 0에 가장 가까운 두 용액의 조합
nums = list(map(int, read().split()))

temp = 10000000001
left = 0; right = n - 1
while left < right:
    sum = nums[left] + nums[right]
    if abs(sum) <= temp:
        temp = abs(sum)
        answer = (nums[left], nums[right])
    if sum > 0:
        right -= 1
    else:
        left += 1

# 음수 두개의 합 중 가장 큰 값
if temp > abs(nums[0] + nums[1]):
    answer = (nums[0], nums[1])
if temp > abs(nums[-1] + nums[-2]):
    answer = (nums[-2], nums[-1])

for i in answer:
    print(i, end=' ')