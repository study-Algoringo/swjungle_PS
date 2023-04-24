def solution(word):
    answer = 0
    word_list = []
    for i in word:
        if i == 'A':
            word_list.append(1)
        if i == 'E':
            word_list.append(2)
        if i == 'I':
            word_list.append(3)    
        if i == 'O':
            word_list.append(4)
        if i == 'U':
            word_list.append(5)
            
    change = [781, 156, 31, 6, 1]        
    for j in range(len(word_list)):
        answer += 1 + (word_list[j]-1) *change[j]
    return answer