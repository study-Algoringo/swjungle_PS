import sys
from itertools import combinations

N = int(sys.stdin.readline())
datas = [ sys.stdin.readline().rstrip() for _ in range(N)]
datas.sort(key=lambda x : len(x))

temp = {}
max_value = 0
for data in datas:
    if data not in temp:
        temp[data] = []
    
    for j in range(N):
        if data == datas[j][:len(data)]:
            temp[data].append(datas[j])

for key in temp.keys():
    result=temp[key]
    answer = 1
    for i in range(N):
        if datas[i] in result:
            continue
        
        result.extend(temp[datas[i]])
        answer+=1
    max_value = max(max_value,answer)
print(max_value)
        
