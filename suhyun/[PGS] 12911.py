from collections import Counter
def solution(n):
    answer = Counter(str(bin(n))[2:])
    while True:
        n+=1
        temp = Counter(str(bin(n))[2:])
        if temp['1'] == answer['1']:
            return n


print(solution(15))