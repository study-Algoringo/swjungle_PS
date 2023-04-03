def solution(citations):
    answer = 0
    citations.sort()
    c = 0
    for i in range(len(citations)):
        if len(citations) - i >= citations[i]:
            c = i 
            
        else:
            break
        
    for k in range(c, 1001):
        for j in range(c, len(citations)+1):
            
            
        
    
    return answer

c = [3, 0, 6, 1, 5]	
solution(c)