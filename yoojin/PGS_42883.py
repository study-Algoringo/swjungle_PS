def solution(number, k):
    answer = ''; cnt = 0
    # 삭제한 횟수가 k보다 작고, 다음 숫자가 나보다 크면 삭제하기
    while cnt < k:
        flag = 0
        for i in range(len(number)-1):
            flag = 1
            if number[i] < number[i + 1]:
                number = number[:i] + number[i+1:]
                cnt += 1
        # 내림차순으로 정렬되어 있지만 cnt가 k보다 큰 경우에 대한 처리
        if flag == 0:
            number = number[:-1]
    answer = number
    
    return answer