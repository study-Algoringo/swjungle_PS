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

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))