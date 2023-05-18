def solution(n):
    answer = bin(n).count('1')
    while True:
        n+=1
        temp = bin(n).count('1')
        if temp == answer:
            return n

print(solution(15))