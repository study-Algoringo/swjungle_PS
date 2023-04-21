def solution(numbers, target):
    answer = 0
    cal = [0]       # 계산해준 숫자 리스트
    for n in numbers:   
        temp = []    # 계산해준 숫자 리스트를 갱신해줄 리스트
        for i in cal: # # 계산해준 숫자 리스트에 numbers의 있는 숫자를 순서대로 계산
            temp.append(i + n)  
            temp.append(i - n)
        cal = temp  # 계산해준 숫자 리스트를 갱신
    for j in cal:
        if j == target:
            answer += 1
    return answer

# solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)