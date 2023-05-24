import sys
read = sys.stdin.readline


s, n = map(int, read().split())
num_list = list(map(int, str(n)))

num = []

num.append([' '+('-') * s + ' '] + [('|'+' '*s+'|')] * s + [' '*(s+2)] + [('|'+' '*s+'|')] * s + [' '+('-') * s + ' '])
num.append([' '*(s+2)] + [' '*(s+1)+('|')] * s + [' ' * (s + 2)] + [' '*(s+1)+('|')] * s + [' '*(s+2)])
num.append([' '+('-')*s+' '] + [' '*(s+1)+('|')] * s +[' '+('-')*s+' '] + [('|')+' '*(s+1)] * s +[' '+('-')*s+' '])
num.append([' '+('-')*s+' '] + [' '*(s+1)+('|')] * s +[' '+('-')*s+' '] + [' '*(s+1)+('|')] * s +[' '+('-')*s+' '])
num.append([' '*(s+2)] + [('|'+' '*s+'|')] * s + [' '+('-')*s+' '] + [' '*(s+1)+('|')] * s + [' '*(s+2)])
num.append([' '+('-')*s+' '] + [('|')+' '*(s+1)] * s +[' '+('-')*s+' '] + [' '*(s+1)+('|')] * s +[' '+('-')*s+' '])
num.append([' '+('-')*s+' '] + [('|')+' '*(s+1)] * s +[' '+('-')*s+' '] + [('|'+' '*s+'|')] * s +[' '+('-')*s+' '])
num.append([' '+('-')*s+' '] + [' '*(s+1)+('|')] * s + [' '*(s+2)] + [' '*(s+1)+('|')] * s + [' '*(s+2)])
num.append([' '+('-')*s+' '] + [('|'+' '*s+'|')] * s +[' '+('-')*s+' '] + [('|'+' '*s+'|')] * s +[' '+('-')*s+' '])
num.append([' '+('-')*s+' '] + [('|'+' '*s+'|')] * s +[' '+('-')*s+' '] + [' '*(s+1)+('|')] * s +[' '+('-')*s+' '])

for row in range(2 *s + 3):
    line = ''
    for digit in num_list:
        line += num[digit][row] + ' '
    print(line)


# ' '--' ' = [' '+('-')*s+' ']
# |''''| = [('|'+' '*s+'|')]
# '    ' = [' '*(s+2)]
# '   '| = [' '*(s+1)+('|')] 
# |'   ' = [('|')+' '*(s+1)]

# # 가로획
# horizontal = ' ' + ''.join('-' * s) + ' '

# # 세로획
# vertical = '\n'.join('|' * s)

# # 더블 세로
# double_vertical = ''
# for i in range(s):
#     double_vertical += '|' + ' ' * s  + '|'
#     double_vertical += '\n'

# for i in str(n):
#     if i == '0':
#         print(horizontal)
#         print(double_vertical, end='')
#         print()
#         print(double_vertical, end='')
#         print(horizontal, end='')

#     if i == '1':
#         print()
#         print(vertical)
#         print()
#         print(vertical)
#         print()

#     if i == '2':
#         print(horizontal)
#         for i in vertical:
#             print(' ' * s, i, end='')
#         print()
#         print(horizontal)
#         print(vertical)
#         print(horizontal)
    
#     if i == '3':
#         print(horizontal)
#         for i in vertical:
#             print(' ' * s, i, end='')
#         print()
#         print(horizontal)
#         for i in vertical:
#             print(' ' * s, i, end='')
#         print()
#         print(horizontal)
    
#     if i == '4':
#         print()
#         print(double_vertical, end='')
#         print(horizontal)
#         for i in vertical:
#             print(' ' * s, i, end='')
#         print()

#     if i == '5':
#         print(horizontal)
#         print(vertical)
#         print(horizontal)
#         for i in vertical:
#             print(' ' * s, i, end='')
#         print()
#         print(horizontal)
    
#     if i == '6':
#         print(horizontal)
#         print(vertical)
#         print(horizontal)
#         print(double_vertical, end='')
#         print(horizontal)

#     if i == '7':
#         print(horizontal)
#         for i in vertical:
#             print(' ' * s, i, end='')
#         print()
#         print()
#         for i in vertical:
#             print(' ' * s, i, end='')
#         print()

#     if i == '8':
#         print(horizontal)
#         print(double_vertical, end='')
#         print(horizontal)
#         print(double_vertical, end='')
#         print(horizontal)
    
#     if i == '9':
#         print(horizontal)
#         print(double_vertical, end='')
#         print(horizontal)
#         for i in vertical:
#             print(' ' * s, i, end='')
#         print()
#         print(horizontal)

# 이렇게 하면 세로로 출력됨!