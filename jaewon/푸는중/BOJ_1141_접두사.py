import sys
sys.stdin=open("/Users/admin/Documents/swjungle_PS/jaewon/푸는중/input.txt", "rt")
input = sys.stdin.readline

n = int(input())
s_list = []
for _ in range(n):
    s_list.append(input().rstrip())
s_list.sort(key=len)

count = n
for i in range(len(s_list)):
    for j in range(i + 1, len(s_list)):
        if s_list[j].startswith(s_list[i]):
            count -= 1
            break
print(count)