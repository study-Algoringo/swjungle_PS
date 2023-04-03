def solution(citations):
    citations.sort()
    cnt = 1
    for i in range(len(citations)):
        for j in range(i, len(citations)):
            if citations[i] < citations[j]:
                h = citations[i]
                tmp = citations.index(citations[i])
                x, y = h, len(citations) - h

    answer = 0
    return answer

citations = [3, 0, 6, 1, 5]

solution(citations)