import sys
input = sys.stdin.readline

n = int(input())

words = [input().rstrip() for _ in range(n)]

words.sort(key=lambda x: len(x))

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if words[j][:len(words[i])] == words[i]:
            print(1,words[i],words[j])
            break
    else:
        print(2,words[i],words[j])
        cnt += 1

print(cnt)
