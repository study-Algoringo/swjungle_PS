def DFS(numbers, target, d) :
    answer = 0
    if d == len(numbers):
        if sum(numbers) == target:
            return 1
        return 0
    else:
        answer += DFS(numbers, target, d + 1)
        numbers[d] *= -1
        answer += DFS(numbers, target, d + 1)
        return answer
    
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer
    
        # res = [0]
    # for i in numbers:
    #     for j in ans:
    #         ans = [0]
    #         ans.append(j + i) # 더하기 노드
    #         ans.append(j - i) # 빼기 노드
    #     res = ans
    # return res.count(target)
