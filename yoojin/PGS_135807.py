import math

def solution(arrayA, arrayB):
    answer = 0
    # arrayA의 최대 공약수 a와 arrayB의 최대 공약수 b 비교,
    gcd_a = arrayA[0]
    for elem in arrayA[1:]:
        gcd_a = math.gcd(gcd_a, elem)

    gcd_b = arrayB[0]
    for elem in arrayB[1:]:
        gcd_b = math.gcd(gcd_b, elem)
    # 만약 arrayB의 어떤 수가 a로 나누어 지거나, arrayA의 수가 B로 나누어지면 더 작은 공약수를 구한다.(공약수의 약수도 공약수)
    for i in range(gcd_a, 1, -1):
        if gcd_a % i == 0 and not divide_all_elem(arrayB, i):
            answer = max(answer, i)
            break    

    for i in range(gcd_b, 1, -1):
        if gcd_b % i == 0 and not divide_all_elem(arrayA, i):
            answer = max(answer, i)
            break

    return answer

# def gcd(arr):
#     # arr에 있는 최소 값을 골라서 해당 값 이하인 수에 대해서 나머지가 0인 가장 큰 값 구하기
#     m = min(arr)
#     for i in range(m, 1, -1):
#         for elem in arr:
#             if elem % i != 0:
#                 break
#         else:
#             return i
#     return 1

def divide_all_elem(arr, num):
    for elem in arr:
        if elem % num == 0:
            break
    else:
        return 0
    return 1