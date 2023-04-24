def solution(number, k):
    n = list(number)
    answer = ''
    i = 0
    while k > 0:
        start = n[i]
        end = n[i+1]
        if (start < end):
            n.remove(start)
            k -= 1
        else:
            n.remove(end)
            k -= 1

    return ''.join(n)
