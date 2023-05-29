def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    # board의 첫 번째 행과 첫 번째 열은 그대로 사용하므로 answer 값 업데이트
    answer = max(board[0])  # 첫 번째 행에서 가장 큰 값
    for i in range(n):
        if board[i][0] == 1:
            answer = 1
            break
    
    # board의 각 칸을 순회하면서 가장 큰 정사각형의 한 변의 길이를 구함
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])
    
    return answer**2
