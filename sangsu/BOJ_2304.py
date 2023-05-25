import sys
input = sys.stdin.readline
gidung = []
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    gidung.append((a,b))
    
gidung.sort()
size = 0
h = 0
s = 0
for j in range(n):
   x = gidung[j][0] 
   y = gidung[j][1]
   if y > h:
       size += h * (x-s)
       h = y
       s = x
       if j == n-1:
           size += y
    
   elif y == h:
       size+= h*(x-s)
       s = x
       if j == n-1:
           size +=y
       
   else:
       if j == n-1:
           
           size += h +(x-s)*y
           h = y
           for i in range(n-2, -1, -1):
               if gidung[i][0] != s:
                   size += (gidung[i][0]-s) *(gidung[i][1]-h)
                   h = gidung[i][1]
               else:
                   break
           
print(size)
# 5

# 13 4
# 6 5
# 4 3
# 11 3
# 9 5