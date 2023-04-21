def solution(phone_book):
    answer = True
    
    # 딕셔너리의 모든 키를 for로 순회하면서, 각 키마다 어떤 로직을 실행해준다.
    # 딕셔너리에서 keys에서 특정 key를 찾는 것은 O(1)이기 때문에 배열을 그대로 사용한 풀이보다 시간복잡도 측면에서 효율적이다.
    phone_dict = {}
    for key in phone_book:
        phone_dict[key] = 1
    
    # 키의(번호) 맨 왼쪽 문자부터 차례대로 하나 씩 늘려가면서(tmp),
    # 각 단계에서 그 것이 딕셔너리의 keys에 존재하는지 판별한다.
    # 만약 존재한다면 해당 키의 접두사가 존재한다는 뜻이므로 False를 리턴한다.
    for phone_num in phone_book:
        tmp = ''
        for num in phone_num:
            tmp += num
            if tmp in phone_book and tmp != phone_num:
                answer = False
                return answer
    
    return answer

solution(["123","1236","7829"])