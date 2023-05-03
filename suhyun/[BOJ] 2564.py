import sys
w, h = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
temp = []
answer = 0

for i in range(N+1):
    x, y = map(int,sys.stdin.readline().split())
    if x == 1:
        temp.append(y)
    elif x == 2:
        temp.append(w+h+w-y)
    elif x == 3:
        temp.append(w+h+w+h-y)
    else:   
        temp.append(w+y)

for i in range(N):
    circle  = abs(temp[-1] - temp[i])
    r_circle = 2*(w+h) - circle
    answer += min(circle,r_circle)

print(answer)