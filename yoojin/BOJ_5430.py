import sys
from collections import deque
read = sys.stdin.readline

t = int(read())

for _ in range(t):
    # 명령 한 줄 입력받기
    flag = 0
    command = list(_ for _ in read().strip())
    n = int(read())
    array = deque(read().strip()[1:-1].split(','))

    for c in command:
        if c == 'R':
            flag += 1
        if c == 'D':
            if len(array) == 0 or n == 0:
                print('error')
                break
            if flag % 2 == 0:
                array.popleft()
            else:
                array.pop()
    else:
        if flag % 2 == 0:
            print('[', ','.join(array), ']', sep='')
        else:
            array.reverse()
            print('[', ','.join(array), ']', sep='')