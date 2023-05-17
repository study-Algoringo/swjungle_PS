# 같은 점수를 맞춰도 중복되지 않음
# 어피치가 맞춘 것 = info 화살의 개수
# bfs
from collections import deque

def bfs(n, info):
    
    q = deque([0, [0,0,0,0,0,0,0,0,0,0,0]])
    # 점수 차 저장하는 변수
    result = 0
    while q:
        a, l = 0
        src, arrow = q.popleft()
        
        # 종료 조건 : 화살을 다 쏜 경우
        if sum(allow) == n:
            for i in range(11):
                if info[i] > arrow[i]:
                    a += 10 - i
                else:
                    l += 10 - i
        
        
def solution(n, info):
    answer = []
    return answer
