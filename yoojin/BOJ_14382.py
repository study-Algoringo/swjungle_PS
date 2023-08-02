import sys
read = sys.stdin.readline

t = int(read())

def sleep_num(n, arr):
    for i in str(n):
        arr[int(i)] = 1
    return arr

for i in range(t):
    num = int(read())
    arr = [0] * 10
    
    cnt = 1
    while arr != [1] * 10:
        new_num = cnt * num
        if num == 0:
            answer = "INSOMNIA"
            break
        arr = sleep_num(new_num, arr)
        cnt += 1
        answer = num * (cnt-1)

    print("Case #{0}: {1}".format((i+1), answer))
    