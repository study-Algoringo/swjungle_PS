import sys
N = int(sys.stdin.readline())
block = []

# 입력 및 정렬 진행
for _ in range(N):
    block.append(list(map(int,list(sys.stdin.readline().split()))))
block.sort()

# 가장 긴 그래프 값 구하기
max_idx = 0
max_len = 0
for i in range(N):
    if max_len < block[i][1]:
        max_len = block[i][1]
        max_idx = i

# 쭉 내려가는 경우
# 쭉 올라가는 경우
# 들쑥 날쑥 한 경우
L_stack = [block[max_idx]]
R_stack = [block[max_idx]]
for i in range(max_idx+1,N):
    if R_stack[-1][1] < block[i][1]:
        R_stack.pop()
    R_stack.append(block[i])

for i in range(max_idx-1,-1,-1):
    if L_stack[-1][1] < block[i][1]:
        L_stack.pop()
    L_stack.append(block[i])

L_stack.sort()
R_stack.sort()
stack = L_stack[:-1] + R_stack

result = 0
for i in range(1,len(stack)):
    x = abs(stack[i][0] - stack[i-1][0])
    y = stack[i-1][1]
    # result += (abs(stack[i][0] - stack[i-1][0]) * stack[i-1][1])
print(result)
