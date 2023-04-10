def solution(phone_book):
    answer = True
    brk = False
    phone_book.sort(key=lambda x: len(x))
    for i in range(len(phone_book)):
        k = len(phone_book[i])
        if brk : 
            break
        for j in range(i+1, len(phone_book)):
            if phone_book[j][:k] == phone_book[i]:
                answer = False
                brk = True
                break
                
        
    return answer
