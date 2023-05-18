# from itertools import combinations_with_replacement 
# def solution(n, info):
#     score_num = [0,1,2,3,4,5,6,7,8,9,10] # 점수판
#     mx_board = []
#     mx_gap = -1

#     for score_list in combinations_with_replacement(score_num, n):
#         lion = 0
#         appeach = 0
        
#         score_board = [0 for _ in range(11)]
#         for score in score_list:
#             score_board[10 - score] += 1
            
#         for i in range(11):
#             if score_board[i] == 0 and info[i] == 0:
#                 continue
#             if score_board[i] > info[i]:
#                 lion += (10 - i)
#             else:
#                 appeach += (10 - i)
        
#         if lion > appeach:
#             gap = lion - appeach
#             if gap > mx_gap:
#                 mx_gap = gap
#                 mx_board = score_board
        
#     return mx_board

from itertools import combinations_with_replacement
def solution(n, info):
    max_score = [-1]
    max_gap = -1
    # scores = [0,1,2,3,4,5,6,7,8,9,10]
    scores = [10,9,8,7,6,5,4,3,2,1,0]
    # 1. 나올 수 있는 스코어의 모든 경우의 수 찾기
    for score in combinations_with_replacement(scores,n):
        score_board = [0 for i in range(11)]
        # 2. 해당 스코어 저장
        for s in score:
            score_board[s] += 1

        # 3. 어피치 점수와 비교 (0이 아닌 경우)
        lion = 0
        appeach = 0
        for i in range(11):
            ## 3-1. 라이언 == 어피치 => 어피치
            if score_board[i] == 0 and info[i] == 0:
                continue
            ## 3-2. 라이언 > 어피치
            elif score_board[i] > info[i]:
                lion+=(10-i)
            ## 3-3. 라이언 < 어피치, 라이언 == 어피치
            else:
                appeach+=(10-i)
        
        # 4. 라이언 > 어피치 (갭 차이 확인)
        if lion > appeach:
            gap = lion - appeach
            if gap > max_gap:
                max_gap = gap
                max_score = score_board
        ## 4-2. max_gap 보다 gap이 크다면 max_gap = gap, max_board = score_board
    return max_score

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))