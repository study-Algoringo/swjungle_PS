def solution(n, words):
    for i in range(1,len(words)):
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]:
            return [i%n+1,i//n+1]
    return [0,0]