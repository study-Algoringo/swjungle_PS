import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan_list = []
for i in range(k):
    m = int(input())
    lan_list.append(m)
max_len = 0
start = 1
end = max(lan_list)

while start <= end:
    
    cnt = 0
    mid = (start + end) // 2
    for lan in lan_list:
        cnt += lan//mid
    
    if cnt >= n:
        start = mid+1
        max_len = max(max_len, mid)
        
    else:
        end = mid-1
        
print(max_len)