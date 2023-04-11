#구현 실패..
def solution(numbers):
        answer = ''
        numbers = list(map(str, numbers))
        numbers.sort(key= lambda  x: x*3, reverse = True)
        for number in numbers:
            answer += number
        
        if answer[0] == "0": 
            answer = "0"
        
        
        
        return answer
    
    
# 1. 정수형으로 되어 있는 리스트를 통째로 str 형식으로 바꾸는 방법  list(map(str, numbers))
# 2. lamda를 이용하여 리스트를 특정 순서대로 정렬하는 방법
# 3. 구현보다 더 효율적인 알고리즘 설계에 시간을 더 투자할 것!
        
print(solution([3, 30, 34, 5, 9]))