from collections import deque

def solution(p):
    answer = ''
    if not p:
        return answer

    while p:
        u, v = separate(p)
        if is_right(u):
            answer += ''.join(_s for _s in u)
            p = v
    
        else:
            answer += '('
            answer += solution(v)
            answer += ')'
            u = u[1:-1]  # 첫 번째와 마지막 문자 제거
            u = reverse_bracket(u)  # 괄호 방향 뒤집기
            answer += ''.join(_s for _s in u)
            break
            
    return answer

def separate(s):
    left_bracket = 0; right_bracket = 0
    ret = []
    s = deque(s)
    while s:
        val = s.popleft()

        if val == '(':
            left_bracket += 1
        elif val == ')':
            right_bracket += 1
        ret.append(val)
        
        if left_bracket == right_bracket:
            return ret, list(s)
    return ret, []

def reverse_bracket(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '(':
            s[i] = ')'
        else:
            s[i] = '('
    return s

def is_right(s):
    l_cnt = 0
    r_cnt = 0
    for _s in s:
        if l_cnt < 0:
            return False
        if l_cnt < 0 or r_cnt < 0:
            return False
        if _s == '(':
            l_cnt += 1
        else:
            l_cnt -= 1
            
    return l_cnt == r_cnt