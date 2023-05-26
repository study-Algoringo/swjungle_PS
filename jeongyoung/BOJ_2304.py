# 창고 다각형 230525
n = int(input())
total = []
for _ in range(n):
    l, h = map(int, input().split())
    total.append([l, h])
total.sort() # x축 기준으로 정렬
index = 0
cnt = 0
result = 0
# 가장 높은 높이의 인덱스 저장하기 - 다른 변수가 아닌 result에 값 저장해야함
# 가장 높은 다각형은 밑의 for문에서 계산해주지 않음!
for i in total:
    if result < i[1]:
        result = i[1]
        index = cnt
    cnt += 1

# 현재 높이보다 더 높은 높이가 들어오면 저장해둔 인덱스와 높이를 곱하기
h = total[0][1]
for i in range(index): # 해당 인덱스 : 제일 높은 높이의 인덱스까지 돌려야함 : 수정 필요
    if h < total[i + 1][1]:
        result += h * (total[i + 1][0] - total[i][0])
        h = total[i + 1][1]
    else:
        result += h * (total[i + 1][0] - total[i][0])

h = total[-1][1]
# 가장 큰 거 만나고 난 뒤 처리
for i in range(n-1, index, -1):
    if h < total[i - 1][1]:
        result += h * (total[i][0] - total[i - 1][0])
        h = total[i - 1][1]
    else:
        result += h * (total[i][0] - total[i - 1][0])

print(result)
