import sys
input = sys.stdin.readline

s, n = map(str, input().split())
s = int(s)
l = len(n)

for i in range(2*s+ 3):
    
    for j in range(l):
        if i == 0:
            if n[j] == '0':
                print(" ", "-" * s, " "," ",end="")
            if n[j] == '1':
                print(" "," "," "," "," ",end="")
            if n[j] == '2':
                print(" ","-" * s," "," ",end="")
            if n[j] == '3':
                print(" ","-" * s," "," ",end="")
            if n[j] == '4':
                print(" "," "," "," "," ",end="")
            if n[j] == '5':
                print(" ","-" * s," "," ",end="")
            if n[j] == '6':
                print(" ","-" * s," "," ",end="")
            if n[j] == '7':
                print(" ","-" * s," "," ",end="")
            if n[j] == '8':
                print(" ","-" * s," "," ",end="")
            if n[j] == '9':
                print(" ","-" * s," "," ",end="")
        elif  i >0 and i < s + 1:
            if n[j] == '0':
                print("|"," "," ","|"," ",end="")
            if n[j] == '1':
                print(" "," "," ","|"," ",end="")
            if n[j] == '2':
                print(" "," "," ","|"," ",end="")
            if n[j] == '3':
                print(" "," "," ","|"," ",end="")
            if n[j] == '4':
                print("|"," "," ","|"," ",end="")
            if n[j] == '5':
                print("|"," "," "," "," ",end="")
            if n[j] == '6':
                print("|"," "," "," "," ",end="")
            if n[j] == '7':
                print(" "," "," ","|"," ",end="")
            if n[j] == '8':
                print("|"," "," ","|"," ",end="")
            if n[j] == '9':
                print("|"," "," ","|"," ",end="")
        elif i == s + 1 :
            if n[j] == '0':
                print(" ", " ", " "," ",end="")
            if n[j] == '1':
                print(" "," "," "," "," ",end="")
            if n[j] == '2':
                print(" ","-" * s," "," ",end="")
            if n[j] == '3':
                print(" ","-" * s," "," ",end="")
            if n[j] == '4':
                print(" ","-" * s," "," ",end="")
            if n[j] == '5':
                print(" ","-" * s," "," ",end="")
            if n[j] == '6':
                print(" ","-" * s," "," ",end="")
            if n[j] == '7':
                print(" "," "," "," ",end="")
            if n[j] == '8':
                print(" ","-" * s," "," ",end="")
            if n[j] == '9':
                print(" ","-" * s," "," ",end="")
        elif i > s +1 and i < 2 * s + 2:
            if n[j] == '0':
                print("|"," "," ","|"," ",end="")
            if n[j] == '1':
                print(" "," "," ","|"," ",end="")
            if n[j] == '2':
                print("|"," "," "," "," ",end="")
            if n[j] == '3':
                print(" "," "," ","|"," ",end="")
            if n[j] == '4':
                print(" "," "," ","|"," ",end="")
            if n[j] == '5':
                print(" "," "," ","|"," ",end="")
            if n[j] == '6':
                print("|"," "," ","|"," ",end="")
            if n[j] == '7':
                print(" "," "," ","|"," ",end="")
            if n[j] == '8':
                print("|"," "," ","|"," ",end="")
            if n[j] == '9':
                print(" "," "," ","|"," ",end="")
        elif i == 2*s + 2:
            if n[j] == '0':
                print(" ", "-" * s, " "," ",end="")
            if n[j] == '1':
                print(" "," "," "," "," ",end="")
            if n[j] == '2':
                print(" ","-" * s," "," ",end="")
            if n[j] == '3':
                print(" ","-" * s," "," ",end="")
            if n[j] == '4':
                print(" ","-" * s," "," ",end="")
            if n[j] == '5':
                print(" ","-" * s," "," ",end="")
            if n[j] == '6':
                print(" ","-" * s," "," ",end="")
            if n[j] == '7':
                print(" "," "," "," ",end="")
            if n[j] == '8':
                print(" ","-" * s," "," ",end="")
            if n[j] == '9':
                print(" ","-" * s," "," ",end="")
        if j == l-1:
            print()