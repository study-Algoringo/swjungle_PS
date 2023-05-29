def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    # board의 첫 번째 행과 첫 번째 열은 그대로 사용하므로 answer 값 업데이트
    answer = max(board[0])  # 첫 번째 행에서 가장 큰 값

    # board의 각 칸을 순회하면서 가장 큰 정사각형의 한 변의 길이를 구함
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer**2

board_one = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board_two = [[0,0,1,1],[1,1,1,1]]
board_three = [[1,1,1,1],[1,1,0,0]]

print(solution(board_three))

# DP 풀이 방법
# def solution(board):
#     dp = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
#     global_max = 0
#     for i in range(1, len(board)+1):
#         for j in range(1, len(board[0])+1):
#
#             if board[i-1][j-1] == 1:
#                 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#
#                 if dp[i][j] > global_max :
#                     global_max = dp[i][j]
#
#     return global_max**2
