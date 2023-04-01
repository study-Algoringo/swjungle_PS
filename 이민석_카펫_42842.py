def solution(brown, yellow):
    a = 1
    b = 0
    while a*b == brown+yellow:
        b = int(brown //2) - a
        if a*b == (brown+yellow):
            answer=[b,a]
            return answer
        a += 1
    
