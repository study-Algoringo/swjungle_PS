from itertools import combinations
def solution(number, k):
    real_list = []
    answer = ''
    num_list = [int(i) for i in number]
    while k and num_list:
        max_num = 0 
        for j in range(k+1):
            max_num = max(max_num, num_list[j])
        p = num_list.index(max_num)
        num_list = num_list[p+1:]
        real_list.append(num_list[p])
        k -= p
        
    str_num = ''.join(map(str, real_list))

    answer += str_num

    
    
    return answer

print(solution("1924", 2))