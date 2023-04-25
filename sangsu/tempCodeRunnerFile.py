import sys
input = sys.stdin.readline
n = int(input())
jubdu = list([] for _ in range(n))
word_list = []
for _ in range(n):
    word_list.append(input())
word_list.sort()

for i in range(n):
    m = len(word_list[i])
    for j in range(i+1, n):
        if word_list[i] == word_list[j][:m]:
            jubdu[i].append(j)
            
        else:
            break
        
real_list = []

for idx in range(0, len(word_list), -1):
    if not word_list[idx]:
        real_list.append(idx)
        
    else:
        for iz in word_list[idx]:
            if iz in real_list:
                break
        else:
            real_list.append(idx)
            
print(len(real_list))
                
                
    