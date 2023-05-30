def solution(board):
    dp = [[0] * len(board[0]) for i in range(len(board))]
    dp[0] = board[0]
    for i in range(len(board)):
        dp[i][0] = board[i][0]
        
    # 현재 pos가 정사각형의 꼭지점이 되는 경우, 최대로 만들 수 있는 정사각형의 개수
    # pos가 1이면 왼위, 위, 왼의 pos만 확인하고 그 중 최솟값을 골라 + 1을 하여 dp 테이블 채우기
    # pos가 0이면 dp 테이블에 0 채우기
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            else:
                dp[i][j] = 0
    answer = max(map(max, dp))**2

    return answer