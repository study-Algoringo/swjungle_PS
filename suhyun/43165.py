#DFS
def dfs(numbers,target,length,total):
    if length == length(numbers):
        if total == target:
            return 1
        return 0
    
    answer+=dfs(numbers[1:],target,length+1,total+numbers)
    answer+=dfs(numbers[1:],target,length+1,total-numbers)

    return answer

def solution(numbers, target):
    answer =  dfs(numbers,target,0,0)
    return answer




# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    
print(solution([1,1,1,1,1],3))