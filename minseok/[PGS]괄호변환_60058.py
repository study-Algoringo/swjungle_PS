def make_str(p):
    open_ = 0
    close_ = 0
    cnt=0
    while True:
        if p[cnt] == '(':
            open_ += 1
        else:
            close_ += 1
        cnt += 1
        if open_ == close_:
            return p[:cnt]
            
def check_str(u):
    o=0
    c=0
    if u[-1] == '(' or u[0] == ')' :
        return False

    for i in range(len(u)):
        if u[i] == '(':
            o += 1
        else: 
            if o == c + 1:
                return True
            if o < c + 1:
                return False
            c += 1


def solution(p):
    answer = ''

    if not p:
        return ''
    
    u=make_str(p)
    v=p[len(u):]
    
    if check_str(u):
        return u+solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer


print(solution("(()())()"))