import sys
read = sys.stdin.readline

t = int(read())

def tidy(n):
    num = list(str(n))
    length = len(num)

    # while True:
    #     num = str(n)
    #     for i in range(len(str(n))-1):
    #         if num[i] >= num[i+1]:
    #             n -= 1
    #             continue
    #     return int(num)
    for i in range(length - 1, 0, -1):
        if num[i - 1] > num[i]:
            num[i - 1] = str(int(num[i - 1]) - 1)
            for j in range(i, length):
                num[j] = '9'

    tidy_num = int(''.join(num))
    return tidy_num

for i in range(t):
    num = int(read())
    tidy_num = tidy(num)
    print("Case #{0}: {1}".format(i+1, tidy_num))