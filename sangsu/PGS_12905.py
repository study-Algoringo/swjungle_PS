def solution(board):
    answer = 1
    n = len(board)
    m = len(board[0])
    for i in range(1, n):
        max_num = 0
        for j in range(m):
            if board[i][j] == 1:
                board[i][j] = board[i-1][j]+ 1
        for k in range(m):
            t = board[i][k]
            if t != 0 and k+t<m+1:
                for e in range(k, k+t):
                    if board[i][e] < t:
                        break
                else:
                    max_num = max(max_num, t)
                    
        answer = max(answer, max_num) 
         
    return answer*answer

print(solution([[0,0,1,1],[1,1,1,1]]))