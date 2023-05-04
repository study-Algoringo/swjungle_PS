import time
def solution(want, number, discount):
    answer = 0
    length = len(discount) - sum(number) + 1
    needs = {}
    for i in range(len(want)):
        needs[want[i]] = number[i]
    
    for i in range(length):
        temp = needs.copy()
        flag = 0
        for j in discount[i:sum(number)+i]:
            if j in temp:
                temp[j] -=1

        for i in temp.values():
            if i !=0:
                flag = 1
                break

        if flag == 0:
            answer+=1

    return answer

# K-상수님의 생각
# def solution(want, number, discount):
#     answer = 0
#     cnt = 0
#     n = len(want)
#     for i in range(len(discount)):
#         if discount[i] in want:
#             j = want.index(discount[i])
#             number[j] = number[j] -1    

#         if i > 9:
#             if discount[i-10] in want:
#                 number[want.index(discount[i-10])] += 1

#         for num in number:
#             if num != 0:
#                 break   
#         else: answer += 1

#     return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))