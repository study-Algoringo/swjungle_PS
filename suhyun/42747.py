def solution(citations):
    answer = 0
    cnt = 0

    citations.sort()

    answer = len(citations)//2

    return answer

print(solution([3, 0, 6, 1, 5]))