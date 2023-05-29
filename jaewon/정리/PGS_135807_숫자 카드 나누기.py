import math

def solution(arrayA, arrayB):
    answer = 0
    gcd_a = 0
    gcd_b = 0

    for i in range(len(arrayA)):
        gcd_a = math.gcd(gcd_a, arrayA[i])

    for j in range(len(arrayB)):
        gcd_b = math.gcd(gcd_b, arrayB[j])

    # 다른 사람 거 나눠지면 안됨
    # gcd 제일 작은 값 1이라 나눠지면 1
    for k in range(len(arrayA)):
        if arrayA[k] % gcd_b == 0:
            gcd_b = 1
        if arrayB[k] % gcd_a == 0:
            gcd_a = 1

    if gcd_a == 1 and gcd_b == 1:
        return 0
    else:
        answer = max(gcd_a, gcd_b)
    return answer

# 유클리드 호제법 -> 최대공약수 나온다.
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

arr1 = [14, 35, 119]
arr2 = [18, 30, 102]

print(solution(arr1, arr2))