def solution(citations):
    citations.sort() #0, 1, 3, 5, 6
    cnt = len(citations) # 전체 논문 수
    answer = 0
    for i in range(cnt):
        if citations[i] >= cnt - i:
            return cnt - i
    return answer
