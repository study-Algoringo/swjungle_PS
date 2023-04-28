def solution(number, k):
    answer = ''; cnt = 0
    # 삭제한 횟수가 k보다 작고, 다음 숫자가 나보다 크면 삭제하기
    num = list(number)
    while k:
        flag = 0
        for i in range(len(num)-1):
            if k == 0: break
            if num[i] < num[i+1]:
                flag = 1
                num.pop(i)
                k -= 1
                
        # 내림차순으로 정렬되어 있지만 cnt가 k보다 큰 경우에 대한 처리
        if flag == 0:
            num.pop()
            k -= 1

    return ''.join(num)

print(solution("1231234", 3))