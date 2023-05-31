def solution(board):

    dp = [[0]* (len(board[0])+1) for _ in range(len(board)+1)]
    global_max = 0
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):

            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                if dp[i][j] > global_max :
                    global_max = dp[i][j]

    return global_max**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))