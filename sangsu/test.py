import math

def solution(n, k):
    answer = 0
    stack = []
    digit_list = getDigitNum(n,k)
    t  = len(digit_list)
    for i in range(t):
        if digit_list[i] != 0:
            stack.append(digit_list[i])
            if i ==t-1:
                partNum = int("".join(map(str, stack)))
                if is_prime(partNum):
                    answer+=1
                
        else:
            if stack:
                partNum = int("".join(map(str, stack)))
                if is_prime(partNum):
                    answer += 1
                stack = []
    
    return answer

def getDigitNum(n, k):
    digit_list = []
    while 1:
        digit_list.append(n%k)
        n = n//k
        if not n:
            digit_list.reverse()
            return digit_list
        

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(solution(110011, 10))
