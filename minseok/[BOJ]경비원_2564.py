import sys
input = sys.stdin.readline


x,y = map(int,input().split())
z = int(input())

n = []
s = []
w = []
e = []

for i in range(z+1):
    a,b = map(int,input().split())
    if i == z and (a in [1,2]):
        dong=[a,b,x-b]
        break
    if i == z and (a in [3,4]):
        dong=[a,b,y-b]
        break

    if a == 1:
        n.append([b,x-b])
    elif a == 2:
        s.append([b,x-b])
    elif a == 3:
        w.append([b,y-b])
    else:
        e.append([b,y-b])
    

ans = 0

while n+s+w+e!=[]:
    if dong[0] == 1:
        if s != []:
            ans += min(dong[1]+s[-1][0]+y,dong[2]+s[-1][1]+y)
            s.pop()
        if n != []:
            ans += abs(n[-1][0]-dong[1])
            n.pop()
        if w != []:
            ans += dong[1]+w[-1][0]
            w.pop()
        if e != []:
            ans += dong[2]+e[-1][0]
            e.pop()
    elif dong[0] == 2:
        if n != []:
            ans += min(dong[1]+n[-1][0]+y,dong[2]+n[-1][1]+y)
            n.pop()
        if s != []:
            ans += abs(s[-1][0]-dong[1])
            s.pop()
        if w != []:
            ans += dong[1]+w[-1][1]
            w.pop()
        if e != []:
            ans += dong[2]+e[-1][1]
            e.pop()
    elif dong[0] == 3:
        if e != []:
            ans += min(dong[1]+e[-1][0]+x,dong[2]+e[-1][1]+x)
            e.pop()
        if w != []:
            ans += abs(w[-1][0]-dong[1])
            w.pop()
        if n != []:
            ans += dong[1]+n[-1][0]
            n.pop()
        if s != []:
            ans += dong[2]+s[-1][0]
            s.pop()
    else:
        if w != []:
            ans += min(dong[1]+w[-1][0]+x,dong[2]+w[-1][1]+x)
            w.pop()
        if e != []:
            ans += abs(e[-1][0]-dong[1])
            e.pop()
        if n != []:
            ans += dong[1]+n[-1][1]
            n.pop()
        if s != []:
            ans += dong[2]+s[-1][1]
            s.pop()
print(ans)