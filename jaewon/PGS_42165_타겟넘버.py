from itertools import permutations

def solution(numbers, target):
    answer = 0
    tmp = []
    cnt = 0
    for i in range(len(numbers)):
        tmp.append(str(numbers[i]))
        tmp.append(str(-numbers[i]))

    tmp = list(set(permutations(tmp, len(numbers))))
    
    for i in range(len(tmp)):
        a = list(map(int, tmp[i]))
        if sum(a) == target:
            cnt += 1
    
    answer = cnt

    return answer

# solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)