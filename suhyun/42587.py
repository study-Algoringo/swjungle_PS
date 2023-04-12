# 숫자가 클 수록 중요하다.
# 처음 0에서 부터 시작한다.
# 대기 목록에서 문서를 꺼내고, J보다 중요도가 높은 문서가 한 개라도 존재하면 다시 맨 뒤로 넣는다. / 없다면 인쇄한다..
from collections import deque
def solution(priorities, location):
    answer = 0
    temp = deque()
    for i in range(len(priorities)):
        temp.append([i,priorities[i]])

    # 뒤에꺼 다 봤는데 우선 순위가 더 높은게 있다면 다시 넣는다.
    # 우선 순위 높은게 없다면 뺀다.
    while temp:
        I,J = temp.popleft()
        flag = 1
        for prioritie in temp:
            if J < prioritie[1]:
                temp.append([I,J])
                flag=0
                break

        if flag:
            answer+=1
            
        if I == location and flag:
            return answer

print(solution([2, 1, 3, 2],2))