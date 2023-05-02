import sys
input = sys.stdin.readline

n = int(input())

lst = []
bigw = 0
bigl = 0
smallw = 0
smalll = 0

for i in range(6):
    lst.append(list(map(int,input().split())))
    if lst[i][0] == 1 or lst[i][0] == 2:
        bigw = max(bigw,lst[i][1])
    if lst[i][0] == 3 or lst[i][0] == 4:
        bigw = max(bigw,lst[i][1])

for j in range(6):
    if j!=0 and j!=5:
        if (lst[j-1][0] == 1 and lst[j+1][0] == 1) or (lst[j-1][0] == 2 and lst[j+1][0] == 2):
            smalll = lst[j][1]
        if (lst[j-1][0] == 3 and lst[j+1][0] == 3) or (lst[j-1][0] == 4 and lst[j+1][0] == 4):
            smallw = lst[j][1]
    if j==0:
        if (lst[-1][0] == 1 and lst[j+1][0] == 1) or (lst[-1][0] == 2 and lst[j+1][0] == 2):
            smalll = lst[j][1]
        if (lst[-1][0] == 3 and lst[j+1][0] == 3) or (lst[-1][0] == 4 and lst[j+1][0] == 4):
            smallw = lst[j][1]  
    if j==5:
        if (lst[j-1][0] == 1 and lst[0][0] == 1) or (lst[j-1][0] == 2 and lst[0][0] == 2):
            smalll = lst[j][1]
        if (lst[j-1][0] == 3 and lst[0][0] == 3) or (lst[j-1][0] == 4 and lst[0][0] == 4):
            smallw = lst[j][1]

print((bigw*bigl-smallw*smalll)*n)



