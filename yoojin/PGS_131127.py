def solution(want, number, discount):
    answer = 0
    # discount의 길이를 처음부터 10까지로 잘라서
    # 해당 배열의 할인 제품들의 개수가 내가 원하는 것과 일치하는 경우 answer+=1
    for i in range(0, len(discount) - 9):
        flag = 1
        count_list = discount[i:i+10]
        for j in range(len(want)):
            if count_list.count(want[j]) != number[j]:
                flag = 0
        if flag == 1:
            answer += 1
        
    return answer