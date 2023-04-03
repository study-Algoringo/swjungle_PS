import sys
input = sys.stdin.readline

n = int(input())

def solution(n):
    if n < 11: # 1~10 까지는 입력값 그대로 출력
        return n

    lst = [0,1,2,3,4,5,6,7,8,9] # 감소하는수 리스트

    cnt = 10

    while True:

        result = []
        # 감소하는 수 리스트 워소 앞에 1~9까지 순서대로 대입
        for i in range(1,10): 
            for j in lst: 
                if j == 9876543210: # 9876543210 보다 큰 감소하는 수는 존재하지 않는다
                    return -1
                if list(map(int, str(j)))[0] < i:  # i가 리스트의 원소의 제일 앞 숫자보다 클 경우 조건 성립      
                    result.append(int(str(i) + str(j))) # 리스트 원소 앞에 i를 붙인뒤 result 리스트에 넣는다 
                    cnt += 1

                    if cnt - 1 == n: 
                        return result[-1]
                else:
                    break
        lst = result # lst 를 result로 변환


print(solution(n))