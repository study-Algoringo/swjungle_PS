def solution(word):
    answer = 0
    aeiou = ['A','E','I','O','U']
    num = [781,156,31,6,1]
    
    for i in range(len(word)):
        for j in range(5):
            if word[i]==aeiou[j]:
                answer += (j)*num[i]+1
            
        
    return answer

