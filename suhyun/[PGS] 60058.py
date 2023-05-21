# 올바른 괄호 확인
def check(data):
    stack = []
    for i in data:
        if i == '(':
            stack.append(i)
        elif stack and i == ')':
            stack.pop()
        elif not stack and i == ')':
            stack.append(i)

    if not stack:
        return 1
    else:
        return 0

# 괄호 반전
def reverse_str(str):
    str = list(str)
    for i in range(len(str)):
        if str[i] == "(":
            str[i] = ")"
        else:
            str[i] = "("

    return ''.join(str)

# 구현 시작
def solution(w):
    open_ = 0
    close_ = 0
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not w:
        return w
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    for i in w:
        if i == "(":
            open_ += 1
        elif i == ")":
            close_ += 1

        if open_ == close_:
            n = open_ * 2
            u = w[:n]
            v = w[n:]
            break
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if check(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u+solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다
        temp = '(' 
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        temp += solution(v)
        # 4-3. ')'를 다시 붙입니다. 
        temp += ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        temp += reverse_str(u[1:-1])
        # 4-5. 생성된 문자열을 반환합니다.
    return temp

    
print(solution("(()())()"))