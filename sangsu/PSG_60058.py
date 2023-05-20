def check(p):
    l = len(p)
    
    cnt = 0
    for i in range(l):
        if p[i] == '(':
            cnt += 1
            
        else:
            cnt -= 1
            if cnt <0:
                return 0
            
    if cnt == 0:
        return 1
    else:
        return 0
            


def reverse(p):
    reversed_string = ""
    for char in p:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
        
    return reversed_string

def course(p):
    n = len(p)
    if n == 0:
        return p
    balance = 0
    for i in range(n):
        if p[i] == '(':
            balance += 1
        else:
            balance -= 1
            
        if balance == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    if check(u):
        return u + course(v)
    
    else:
        return '('+ course(v)+ ')' + reverse(u[1:-1])


def solution(p):
    return course(p)

print(solution("()))((()"))