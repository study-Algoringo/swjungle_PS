import sys
input = sys.stdin.readline

m, n = map(int, input().split())
lesson_list = list(map(int, input().split()))



start = lesson_list[0]
end = sum(lesson_list)
while start <= end:
    mid = (start +end) // 2
    sum_lesson = 0
    cnt = 1
    for i in range(m-1, -1, -1 ):
        sum_lesson += lesson_list[i]
        if sum_lesson > mid:
            cnt += 1
            sum_lesson = lesson_list[i]
            
    if cnt > n:
        start = mid + 1
        
    else:
        end = mid -1
        
print(start)