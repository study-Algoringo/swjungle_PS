from collections import deque
def solution(word):
    answer = 0
    moeum = 'AEIOU'
    result = []
    que = deque('AEIOU')
    print(que)
    while que:
        x = que.popleft()
        result.append(x)
        if len(x) == 5:
            continue

        temp = ''
        for i in range(5):
            temp = x+moeum[i]
            que.append(temp)

    result.sort()     
    for data in result:
        answer+=1
        if data == word:
            break
    return answer



print(solution("EIO"))
