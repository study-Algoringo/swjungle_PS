import sys
n,s = sys.stdin.readline().rstrip().split()

n = int(n)
s = list(s)

number = ['' for _ in range(5)]
number[0] = ' ' + '-'*n + ' ' + ' '
number[1] = ' ' + ' '*n + '|' + ' '
number[2] = '|' + ' '*n + ' ' + ' '
number[3] = '|' + ' '*n + '|' + ' '
number[4] = ' ' + ' '*n + ' ' + ' '

result = [[] for _ in range(5)]
# 0,1,2,3,4,5,6,7,8,9
result[0] = [number[0],number[4],number[0],number[0],number[4],number[0],number[0],number[0],number[0],number[0]]
result[1] = [number[3],number[1],number[1],number[1],number[3],number[2],number[2],number[1],number[3],number[3]]
result[2] = [number[4],number[4],number[0],number[0],number[0],number[0],number[0],number[4],number[0],number[0]]
result[3] = [number[3],number[1],number[2],number[1],number[1],number[1],number[3],number[1],number[3],number[1]]
result[4] = [number[0],number[4],number[0],number[0],number[4],number[0],number[0],number[4],number[0],number[0]]

for i in s:
    print(result[0][int(i)],end='')
print()
for i in range(n):
    for j in s:
        print(result[1][int(j)],end='')
    print() 

for i in s:
    print(result[2][int(i)],end='')
print()

for i in range(n):
    for j in s:
        print(result[3][int(j)],end='')
    print()

for i in s:
    print(result[4][int(i)],end='')




