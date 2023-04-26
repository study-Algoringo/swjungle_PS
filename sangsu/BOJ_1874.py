import sys
input = sys.stdin.readline



n = int(input())
stack = []
i = 1
result = ''

for _ in range(n):
    num = int(input())
    
    while i <= num:
        stack.append(i)
        result += '+\n'
        i += 1
        
    if stack[-1] == num:
        stack.pop()
        result += '-\n'
        
    else:
        result = 'NO'
        break
    
print(result)