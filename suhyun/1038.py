# 민석 오빠의 아이디어로 재구현
import sys
N = int(sys.stdin.readline())


def solution(N):
    lst= [0,1,2,3,4,5,6,7,8,9]
    if N < 10:
        return N

    cnt = 10

    while True:
        # 10의 자릿수 위치
        temp = []
        for i in range(1,10):
            for j in lst:
                if int(j[0]) < i:
                    temp.append(str(i)+str(j))   
                    cnt+=1
                
                if cnt -1 == N:
                    return temp[-1]

                else:
                    break
                
        lst = temp
        
print(solution(N))