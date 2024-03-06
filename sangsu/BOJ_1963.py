import sys
input = sys.stdin.readline
from collections import deque



def is_sosu(number):
    if number < 2:
        return False
    
    for i in range(2, int(number **0.5)+1):
        if number %i ==0:
            return False
        
    return True

def change_one(number):
    result = []
    str_number = str(number)
    num_1 = int(str_number[0])
    for i in range(1, num_1):
        result.append(number - (i*1000))
        
    for i in range(1, 10-num_1):
        result.append(number +(i*1000))
        
    num_2 = int(str_number[1])
    for i in range(1, num_2+1):
        result.append(number - (i*100))
    
    for i in range(1, 10-num_2):
        result.append(number +(i*100))
        
    num_3 = int(str_number[2])
    for i in range(1, num_3+1):
        result.append(number - (i*10))
    
    for i in range(1, 10-num_3):
        result.append(number +(i*10))
    
    num_4 = int(str_number[3])
    for i in range(1, num_4+1):
        result.append(number - (i))
    
    for i in range(1, 10-num_4):
        result.append(number +(i))

    return result
        

n = int(input())
for i in range(n):
    visited = [99999] * 10000
    sosu_1, sosu_2 = map(int, input().split())
    visited[sosu_1] = 0
    que = deque([(sosu_1, 0)])
    while que:
        sosu, k = que.popleft()
        results = change_one(sosu)
        for result in results:
            if is_sosu(result) and visited[result] == 99999:
                que.append((result, k+1))
                visited[result] = k+1
    if visited[sosu_2] == 99999:
        print("Impossible")
    else:
        print(visited[sosu_2])
        


    