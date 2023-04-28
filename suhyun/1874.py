import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
stack = []
result = []
cnt=0

for i in range(1,N+1):
    stack.append(i)
    result.append('+')    
    
    while stack and stack[-1] == arr[cnt]:
        stack.pop()
        result.append('-')
        cnt+=1
        
if stack:
    print("NO")
else:
    print(*result,sep='\n')