import sys
read = sys.stdin.readline

l, c = map(int, read().split())
arr = list(read().split())
answer = []

def solution(index, word):
    if index >= c:
        return
    
    new_word = word + arr[index]

    if len(new_word) == l:
        answer.append(new_word)

    solution(index + 1, word)
    solution(index + 1, new_word)

solution(0, '')
answer.sort()
for a in answer:
    print(a)