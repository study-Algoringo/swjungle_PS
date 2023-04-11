from collections import deque

def solution(numbers):
    answer = -1
    numbers.sort(reverse=True)
    print(numbers)
    temp = deque(map(str,numbers))
    
    length = len(temp)
    for i in range(length):
        a = temp.popleft()
        result=a
        for j in range(len(temp)):
            result+=temp[j]
        
        answer = max(answer,int(result))
        temp.append(a)

    return str(answer)

# def solution(numbers):
#     # 1. 모든 수를 문자열로 변환
#     numbers = list(map(str, numbers))

#     # 2. x+y와 y+x를 비교하여 정렬
#     numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
#     # 3. 정렬된 numbers를 이어붙인 뒤 반환
#     answer = ''.join(numbers)

#     # 0이 여러개일 경우, "000" 대신 "0"을 반환하도록 예외처리
#     if answer[0] == '0':
#         return '0'
#     else:
#         return answer

print(solution([3, 30, 5, 9, 34]))