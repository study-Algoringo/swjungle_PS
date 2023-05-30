def solution(board):
    answer = 0
    row_len = len(board)
    col_len = len(board[0])

    if row_len < 2 or col_len < 2:
        return 1

    for i in range(1, row_len):
        for j in range(1, col_len):
            # 만약 자신의 위치(현재 인덱스)의 값이 1 이상일 경우
            if board[i][j] != 0:
                # 왼쪽상단, 위쪽, 왼쪽의 최솟값을 구한 후 자신의 위치에 최솟값 + 1
                min_val = min(board[i-1][j-1], board[i-1][j], board[i][j-1])
                board[i][j] = min_val + 1
            # 할당한 값의 최댓값을 answer에 할당
            if answer < board[i][j]:
                answer = board[i][j]
    
    # 정사각형의 넓이를 구한다.
    return answer * answer
