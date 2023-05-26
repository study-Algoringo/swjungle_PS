def solution(arrayA, arrayB):
    num = 1
    answer = 0

    while(1):
        num += 1
        a_cnt = 0
        n_a_cnt = 0
        b_cnt = 0
        n_b_cnt = 0

        # arrayA의 모든 원소가 나누어 떨어진다면
        for num_A in arrayA:
            if num_A % num == 0:
                a_cnt += 1
            else:
                n_a_cnt += 1
        
        for num_B in arrayB:
            if num_B % num != 0:
                b_cnt += 1
            else:
                n_b_cnt += 1
        
        if a_cnt == len(arrayA) and b_cnt == len(arrayB):
            answer = num
        elif n_a_cnt == len(arrayA) and n_b_cnt == len(arrayB):
            answer = num

    return answer

arr1 = [14, 35, 119]
arr2 = [18, 30, 102]

print(solution(arr1, arr2))