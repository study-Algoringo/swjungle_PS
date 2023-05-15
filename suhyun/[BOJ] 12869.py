# from itertools import permutations


# def answer(x, y, z, cnt):
#     global ans
#     # x,y,z가 모두 0보다 작은 경우 ans 처리
#     if x <= 0 and y <= 0 and z <= 0:
#         if ans > cnt:
#             ans = cnt
#             return
            
#     # 0보다 작은 인자인 경우 해당 값들을 초기화
#     x = 0 if x <= 0 else x
#     y = 0 if y <= 0 else y
#     z = 0 if z <= 0 else z

#     # 현재 cnt 값이 dp[x][y][z] 보다 클 때, 최소 한 번은 계산 한 경우 return 
#     if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
#         return

#     dp[x][y][z] = cnt

#     # 모든 경우의 수 빼면서 재귀 진행하기
#     for i in permutations([9, 3, 1], 3):
#         answer(x - i[0], y - i[1], z - i[2], cnt + 1)


# N = int(input())
# a = list(map(int, input().split()))
# while len(a) < 3:
#     a += [0]
# ans = 100
# dp = [[[100] * (max(a) + 1) for i in range((max(a) + 1))] for j in range((max(a) + 1))]
# answer(a[0], a[1], a[2], 0)
# print(ans)

from itertools import permutations
def dfs(x,y,z,cnt):
    global ans
    if x <=0 and y <=0 and z<=0:
        if ans > cnt:
            ans = cnt
            return

    x=0 if x <=0 else x
    y=0 if y <=0 else y
    z=0 if z <=0 else z

    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return
    
    dp[x][y][z] = cnt

    for a,b,c in permutations([9,3,1],3):
        dfs(x - a, y - b, z - c, cnt + 1)


N = int(input())
arr = list(map(int,input().split()))
while len(arr) < 3:
    arr += [0]
ans = 61
dp = [[[61] * (61) for _ in range(61)] for _ in range(61)]
dfs(arr[0],arr[1],arr[2],0)
print(ans)






