def solution(citations):
    
    length = len(citations)
    citations.sort()
    # citations[i] 뒤에 남은 숫자가 len(citations) - (citations[i] 앞에 남은 숫자) 보다 클경우 값 출력 
    for i in range(length):
        if citations[i] >= length-i:  
            return length-i
    
    return 0
