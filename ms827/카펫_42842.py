def solution(brown, yellow):
    a = 1 #세로
    b = 0 #가로
    
    # 갈색 격자 = 2a+2b-4 = a+b-2
    # 노란색 격자 = (a-2)(b-2)
    while True:
        b = int(brown //2) - a + 2 
        if a*b == (brown+yellow): # a*b와 갈색,노란색 격자를 더한 값이 같으면 종료
            answer=[b,a]
            return answer
        a += 1
