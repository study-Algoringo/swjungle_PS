# # 시간 초과
# def solution(arrayA, arrayB):
#     minA = min(arrayA)+1
#     minB = min(arrayB)+1
#     max_value = 0
#     for i in range(2,minA):
#         flag = 0
#         for j in arrayA:
#             if j%i !=0:
#                 flag = 1
#                 break
        
#         for j in arrayB:
#             if j%i ==0:
#                 flag = 1
#                 exit()
#         if flag == 0 and i > max_value:
#             max_value = i
            
#     for i in range(2,minB):
#         flag = 0
#         for j in arrayB:
#             if j%i !=0:
#                 flag = 1
#                 break
        
#         for j in arrayA:
#             if j%i ==0:
#                 flag = 1
#                 break
            
#         if flag == 0 and i > max_value:
#             max_value = i

#     return max_value

# 수정
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(arrayA, arrayB):
    a = arrayA[0]
    for i in range(1, len(arrayA)):
        a = gcd(a, arrayA[i])

    b = arrayB[0]
    for i in range(1, len(arrayB)):
        b = gcd(b, arrayB[i])

    for i in range(len(arrayA)):
        if arrayA[i] % b == 0:
            b = 1
        if arrayB[i] % a == 0:
            a = 1
    
    if a == 1 and b == 1:
        return 0
    else:
        return max(a,b)

print(solution([10, 20],[5, 4]))