from itertools import permutations
def sosu(data):
    for i in range(2,data):
        if data%i == 0:
            return 0
    return 1 

def solution(numbers):
    answer = 0
    dp = [0,1]
    results = []
    for i in range(1,len(numbers)+1):
        results.extend(list(map(list,permutations(numbers,i))))
    

    for result in results:
        x = int("".join(result))
        if x not in dp and sosu(x):
            dp.append(x)
            answer+=1 

    return answer

# 다른 사람의 풀이
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)

print(solution("17"))