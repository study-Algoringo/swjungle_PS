from itertools import permutations  
def sosu(x):
        if x<2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    



def solution(numbers):
    answer = 0
    nums = [int(num) for num in numbers]
    for i in range(1, len(numbers)+1):
        num_list = list(permutations(nums, i))
        num_list = set(num_list)
        for numnum in num_list:
            if sosu(int(numnum)):
            
                answer += 1
         
    
    
        
    return answer


print(solution('17'))