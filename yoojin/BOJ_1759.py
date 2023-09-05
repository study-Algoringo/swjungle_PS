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
        if is_password(new_word):
            answer.append(sorted(new_word))

    solution(index + 1, word)
    solution(index + 1, new_word)

def is_password(word):
    vowels = "aeiou"
    num_vowels = sum(1 for char in word if char in vowels)
    num_consonants = len(word) - num_vowels
    return num_vowels >= 1 and num_consonants >= 2

solution(0, '')
answer.sort()
for a in answer:
    print(''.join(a))