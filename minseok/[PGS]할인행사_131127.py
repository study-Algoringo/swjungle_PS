from collections import Counter 
def solution(want, number, discount):
    answer = 0
    dic = {}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    for j in range(len(discount)-9):
        if dic == Counter(discount[j:j+10]):
            answer+=1
    if answer == 0:
        return 0
    return answer
