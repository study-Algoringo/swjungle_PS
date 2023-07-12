def solution(n):
    answer = 0
    
    num_list = []
    while(1):
        if n%2 == 0:
            num_list.append(0)
            n = n//2
            if n == 0:
                break
            
        else:
            num_list.append(1)
            n = n//2
            if n == 0:
                break
    l = len(num_list)

    print(num_list)
    for i in range(0, l-1):
        if num_list[i] == 1 and num_list[i+1] == 0:
            num_list[i] = 0
            num_list[i+1] = 1
            break
    else:
        num_list[-1] = 0
        num_list.append(1)        
        l += 1
    
    for j in range(l):
        answer += (2**j) * num_list[j]
        
    return answer

print(solution(78))