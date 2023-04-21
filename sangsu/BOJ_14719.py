import sys
input = sys.stdin.readline

h, w = map(int, input().split())


block_list = list(map(int, input().split()))
ans = 0
for i in range(max(block_list)):
    tmp = 0
    block = False
    for j in range(len(block_list)):
        if block_list[j]:
            block = True
            ans += tmp
            tmp = 0
            block_list[j] -= 1
            
        elif block and not block_list[j]:
            tmp += 1
            
print(ans)
                
                
                
            
    
    

