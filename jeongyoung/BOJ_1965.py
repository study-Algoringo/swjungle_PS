#[BOJ] 상자넣기 / Silver 2 / 1965 / 박정영

# 앞 < 뒤 앞에 있는 상자를 뒤에 있는 상자 안에 넣을 수 있다
# 1 5 2 3 7

# 최장 길이 증가 수열

n = int(input())
box = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]: # 뒷 박스가 앞 박스보다 크면
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
