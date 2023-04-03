def solution(citations):
    # reverse 정렬 후 해당 원소의 인덱스+1보다 원소의 값이 더 큰 경우, ans를 갱신한다.
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer = i + 1
    
    return answer