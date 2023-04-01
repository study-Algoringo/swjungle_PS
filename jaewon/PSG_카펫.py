import sys
input = sys.stdin.readline

def solution(brown, yellow):
    answer = []
    a = 0
    b = 0
    if yellow == 1:
        answer.append(3)
        answer.append(3)
        return answer

    for j in range(1, yellow):
        if yellow % j == 0:
            a = j
            b = yellow // j
            w = a * 2
            h = b * 2
            if brown == w + h + 4:
                if b+2 in answer:
                    break
                elif a+2 in answer:
                    break
                else:
                    answer.append(b+2)
                    answer.append(a+2)
    return answer

print(solution(8, 1))