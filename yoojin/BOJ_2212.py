import sys
read = sys.stdin.readline

ans = 0
n = int(read())
k = int(read())
nums = list(map(int, read().split()))
nums.sort()

distance = []; division = []

# 거리 차이 큰 순으로 정렬, k-1개를 제거하기
for i in range(1, len(nums)):
    distance.append(nums[i] - nums[i-1])

distance.sort()
print(sum(distance[:n-k]))

# for i in range(k-1):
#     max_elem = max(distance)
#     division.append(distance.index(max_elem) + i)
#     distance.remove(max(distance))

# # 남은 그룹들에 대해 (가장 큰) - (가장 작은)을 더하기
# ans += nums[division[0]] - nums[0]
# ans += nums[-1] - nums[division[-1] + 1]
# for i in range(1, len(division)):
#     ans += nums[division[i]] - nums[division[i-1]+1]

# print(ans)