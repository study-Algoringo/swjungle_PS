def solution(S):
    stack = []
    for char in S:
        stack.append(char)
        while len(stack) >= 2 and ((stack[-2] == 'A' and stack[-1] == 'B') or (stack[-2] == 'B' and stack[-1] == 'A') or (stack[-2] == 'C' and stack[-1] == 'D') or (stack[-2] == 'D' and stack[-1] == 'C')):
            stack.pop()
            stack.pop()
    return ''.join(stack)
print(solution("CBACD"))  # "C"
print(solution("CABABD"))  # ""
print(solution("ACBDACBD"))  # "ACBDACBD"