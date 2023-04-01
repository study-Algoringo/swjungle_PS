def solution(brown, yellow):
    answer = []
    total = brown+yellow
    long = 0
    for i in range(1,yellow+1):
        if yellow/i >= i:
             if yellow%i == 0:
                   long = yellow/i
                   if (i+2)*(long+2) == total:
                    answer.append(long+2)
                    answer.append((i+2))
        
                   
        else:
            break
    return answer
