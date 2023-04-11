from itertools import permutations
def solution(numbers):
    answer = []
    num = list(permutations(numbers, len(numbers)))
    for i in num:
        answer.append("".join(map(str, i)))
    return max(answer)
