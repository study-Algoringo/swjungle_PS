# 숫자가 클 수록 중요하다.
# 처음 0에서 부터 시작한다.
# 대기 목록에서 문서를 꺼내고, J보다 중요도가 높은 문서가 한 개라도 존재하면 다시 맨 뒤로 넣는다. / 없다면 인쇄한다..
from collections import deque
def solution(priorities, location):
    answer = 0
    # 프린터 목록과 우선순위를 함께 넣는다.
    temp = deque((i,data) for i,data in enumerate(priorities))

    # 우선 순위 높은게 없다면 뺀다.
    while temp:
        I,J = temp.popleft()
        # flag = 큰게 있는지 확인
        flag = 1

        # 목록을 확인 후 우선 순위가 높은게 있다면 다시 append
        for prioritie in temp:
            if J < prioritie[1]:
                temp.append([I,J])
                flag=0
                break
        # 높은게 없다면 +1
        if flag:
            answer+=1

        # 찾는 출력물과 동일하면서 temp안에 가장 우선순위가 높다면 정답 
        if I == location and flag:
            return answer

print(solution([2, 1, 3, 2],2))