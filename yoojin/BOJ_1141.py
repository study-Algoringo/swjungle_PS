import sys
read = sys.stdin.readline

n = int(read()); words = []; answer = 0
for i in range(n):
    word = read().strip()
    words.append(word)
words.sort(key=lambda x: len(x))

for i in range(len(words)):
    flag = False
    for j in range(i+1, len(words)):
        if words[i] == words[j][:len(words[i])]:
            flag = True
            break

    if not flag:
        answer += 1
print(answer)