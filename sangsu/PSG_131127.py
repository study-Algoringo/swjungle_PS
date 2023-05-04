def solution(want, number, discount):
    answer = 0
    
    n = len(want)
    goal = [0] *n
    for i in range(len(discount)):
        if discount[i] in want:
            number[want.index(discount[i])] -= 1
            
        if i>9 and discount[i-10] in want:
            
            number[want.index(discount[i-10])] += 1
            
        if number == goal:
            answer += 1
        
        
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))