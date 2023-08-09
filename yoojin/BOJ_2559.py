import sys
read = sys.stdin.readline

n, k = map(int, read().split())
temps = list(map(int, read().split()))

# 현재 temp에서 포함/포함하지 않는 경우의 max 값을 dp 배열에 저장

result = []
# 연속된 k개로 끊어서 모든 조합의 수 계산
partial_sum = sum(temps[:k])
result.append(partial_sum)

for i in range(k, len(temps)):
    # 현재 sum에서 이전거 빼고 다음거 넣기
    partial_sum = partial_sum - temps[i-k] + temps[i]
    result.append(partial_sum)

print(max(result))