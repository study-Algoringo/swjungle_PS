import sys
def solution(n,m,video):
    left, right = max(video), sum(video)

    while left <= right:
        mid = (left+right) // 2
        temp = 0
        cnt = 0

        for x in video:
            if temp + x > mid:
                cnt+=1
                temp = x
            else:
                temp+=x
        
        if cnt >= m:
            left = mid + 1
        else:
            right = mid-1

    return left

n,m  = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
print(solution(n,m,arr))
