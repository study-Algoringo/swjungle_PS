import sys
read = sys.stdin.readline

n, m = map(int, read().split())
records = list(map(int, read().split()))

start = max(records)
end = sum(records)

def divide_to(num):
    idx = 0; count = 0
    while idx < n:
        save = 0
        while idx < n and save + records[idx] <= num:
            save += records[idx]
            idx += 1
        count += 1
    return count <= m

def binary_search(records, start, end, m):
    result = 0
    while start <= end:
        middle = (start + end) // 2
        # 저장할 수 있다면, 값 줄이기
        if divide_to(middle):
            result = middle
            end = middle - 1
        # 저장할 수 없다면, 값 늘리기
        else:
            start = middle + 1
    return result
    
answer = binary_search(records, start, end, m)
print(answer)