import sys
read = sys.stdin.readline

def paint_non_empty_row(cake, r, c):
    for j in reversed(range(c)):
        if cake[r][j] == '?':
            cake[r][j] = cake[r][j + 1]
        else:
            break
    for j in range(c+1, len(cake[r])):
        if cake[r][j] == '?':
            cake[r][j] = cake[r][j - 1]
        else:
            break

def paint_empty_row(cake, r, c):
    for i in reversed(range(r)):
        if cake[i][c] == '?':
            cake[i] = cake[i + 1]
        else:
            break
    for i in range(r+1, len(cake)):
        if cake[i][c] == '?':
            cake[i] = cake[i - 1]
        else:
            break

def solution():
    r, c = map(int, read().split())
    cake = []
    initials = []
    
    for i in range(r):
        cake.append(list(read().strip()))
        for j in range(c):
            if cake[i][j] != '?':
                initials.append((i, j))
    for r, c in initials:
        paint_non_empty_row(cake, r, c)
    for r, c in initials:
        paint_empty_row(cake, r, c)
    return cake
    
for case in range(int(read())):
    print("Case #%d: " % (case + 1))
    for row in solution():
        print(''.join(row))