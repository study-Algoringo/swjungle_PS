def solution(want, number, discount):
    answer = 0
    cnt = 0
    n = len(want)
    for item in discount:
        cnt+= 1
        if item in want:
            i = want.index(item)
            number[i] = number[i] -1    
            
        if cnt > 10:
            if discount[discount.index(item)-10] in want:
                number[want.index(discount[discount.index(item)-10])] = number[want.index(discount[discount.index(item)-10])] + 1
        
        for num in number:
            if num != 0:
                break   
        else: answer += 1
        
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))