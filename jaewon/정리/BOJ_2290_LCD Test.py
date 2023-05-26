import sys
sys.stdin=open("/Users/admin/Documents/swjungle_PS/jaewon/푸는중/input.txt", "rt")
input = sys.stdin.readline

s, n = map(int, input().split())
n = list(str(n))

# 최상단 만들기
for i in n:
    if i == '1' or i == '4':
        print(" " * ((s + 2) + 1), end='')
    elif i == '2' or i == '3' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0':
        print(" " + ("-" * s) + " " + " ", end='')

print()

# 상단 만들기 * s줄 만들기
for _ in range(s):
    for i in n:
        if i == '1' or i == '2' or i == '3' or i == '7':
            print(" " * ((s + 2) - 1) + "|" + " ", end='')
        elif i == '4' or i == '8' or i == '9' or i == '0':
            print("|" +  " " * s + "|" + " ", end='')
        elif i == '5' or i == '6':
            print("|" + " " * (s + 2), end='')
    print()

# 숫자의 중간 1줄 만들기
for i in n:
    if i == '1' or i == '7' or i == '0':
        print(" " * ((s + 2) + 1), end='')
    elif i == '2' or i == '3' or i == '5' or i == '6' or i == '4' or i == '8' or i == '9':
        print(" " + ("-" * s) + " " + " ", end='')

print()

# 하단 만들기 * s줄 만들기
for _ in range(s):
    for i in n:
        if i == '1' or i == '3' or i == '4' or i == '5' or i == '7' or i == '9':
            print(" " * ((s + 2) - 1) + "|" + " ", end='')
        elif i == '6' or i == '8' or i == '0':
            print("|" +  " " * s + "|" + " ", end='')
        elif i == '2':
            print("|" + " " * (s + 2), end='')
    print()

tmp = []
# 최하단 만들기
for i in n:
    if i == '1' or i == '4' or i == '7':
        print(" " * ((s + 2) + 1), end='')
    elif i == '2' or i == '3' or i == '5' or i == '6' or i == '8' or i == '9' or i == '0':
        print(" " + ("-" * s) + " " + " ", end='')
# 문제 접근법
# 숫자의 최상단 1줄/ 숫자의 상단 * s줄 / 숫자의 중간 1줄 / 숫자의 하단 * s줄 / 숫자의 최하단 1줄

#  1234567890
#       --   --        --   --   --   --   --   --  
#    |    |    | |  | |    |       | |  | |  | |  | 
#    |    |    | |  | |    |       | |  | |  | |  | 
#       --   --   --   --   --        --   --       
#    | |       |    |    | |  |    | |  |    | |  | 
#    | |       |    |    | |  |    | |  |    | |  | 
#       --   --        --   --        --   --   --  