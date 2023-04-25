import sys

n = int(sys.stdin.readline())
words = [(sys.stdin.readline()).rstrip() for _ in range(n)]

# 다른단어의 접두사가 되는 단어는 항상 다른단어보다 크기가 작거나 같다.
# 따라서 문자열의 길이가 짧은 순서대로 정렬을 하고, 자기 위치보다 뒤에있는 단어와만 비교한다.
words.sort(key=len)
res = 0
result = []
# 반복문을 통해 단어를 확인
for i in range(n):
    flag = False
    # 현재 단어보다 길이가 긴 단어를 확인
    for j in range(i + 1, n):
        # 현재 단어가 접두사인지 확인
        if words[i] == words[j][0:len(words[i])]:
            flag = True
            result.append(words[i])
            break
    
    # 현재 단어가 접두사가 아니라면 res 카운트
    if not flag:
        res += 1
print(result)
print(res)