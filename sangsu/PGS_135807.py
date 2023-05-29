# def solution(arrayA, arrayB):
#     answer = 0
    
#     arrayA.sort()
#     arrayB.sort()
#     Amax, Bmax = 0, 0
#     for i in range(2, arrayA[0]+1):
#         for A in arrayA:
#             if A%i:
#                 break
#         else:
#             for B in arrayB:
#                 if B%i ==0:
#                     break
#             else:
#                 Amax = i
    
    
#     for j in range(2, arrayB[0]+1):
#         for B in arrayB:
#             if B%j:
#                 break
#         else:
#             for A in arrayA:
#                 if A%j ==0:
#                     break
#             else:
#                 Bmax = j         
                
#     answer = max(Amax, Bmax)
    
#     return answer



import math

def solution(arrayA,arrayB):
    answer = 0
    gc,vc= 0,0
    se = []

    for i in range(len(arrayA)):
        gc = math.gcd(gc,arrayA[i])

    for i in range(len(arrayB)):
        vc = math.gcd(vc,arrayB[i])

    for j in range(len(arrayA)):
        if arrayA[j] % vc == 0:
            vc = 1
        if arrayB[j] % gc == 0:
            gc = 1

    if gc == 1 and vc ==1:
        return 0
    else:
        return max(gc,vc)

# print(solution([14,35,119], [18, 30, 102]))

# 유클리드 호재법
# def gcd(a,b):
    # while b>0:
    #     a,b = b, a%b
    # return a