from itertools import permutations

def solution(numbers):
    answer = 0
    number = list(numbers)
    p_lst = []
    # number 리스트 원소로 만들 수 있는 모든 숫자 조합을 리스트에 채워준다
    for i in range(1,len(number)+1):
        p_lst+=list(map(''.join,permutations(number,i)))
    
    # 같은 숫자 제거
    p_lst=list(set(map(int,p_lst)))
    
    # 소수 찾기
    for i in p_lst:
        if i == 2:
            answer += 1
        elif i <= 1:
            continue
        else:
            for j in range(2,i):
                if i % j ==0:
                    break;
                elif j==i-1:
                    answer += 1
    return answer
