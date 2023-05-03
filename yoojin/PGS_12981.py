def solution(n, words):
    answer = []
    already = []
    
    # 이전에 나왔던 단어이거나 글자 수가 1개면 멈추기
    i = 0
    for i in range(len(words)):
        if len(words[i]) == 1 or already.count(words[i]) != 0:
            break
        if i > 0 and words[i-1][-1] != words[i][0]:
            break
        already.append(words[i])
        i += 1
    print(i)
    if i < len(words):
        answer = ([i % n + 1, i // n + 1])
    else:
        answer = ([0, 0])

    return answer