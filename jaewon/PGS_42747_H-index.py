def solution(citations):
    # citations : 논문이 인용된 횟수가 들어있는 배열
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        # 여기서 i + 1이 h인덱스가 된다.
        # [6, 5, 3, 1, 0] -> 정렬한 배열
        # [1, 2, 3, 4, 5] -> 인덱스 번호
        # 아래 조건문으로 비교하여 h인덱스 갱신
        # 정의 : 인덱스가 3이라면 3번이상 인용된 논문의 개수가 3편 이상이고 나머지 논문이 3평 이하로 인용되면 h인덱스가 된다.
        if citations[i] >= i + 1:
            answer = i + 1
    return answer

citations = [3, 0, 6, 1, 5]

solution(citations)