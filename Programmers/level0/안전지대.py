def solution(board):
    n = len(board)
    answer = n * n
        
    #상, 하, 좌, 우, 상좌, 상우, 하좌, 하우
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
        
            
    data = [[0] * n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                data[x][y] = 1
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        data[nx][ny] = 1
        
    for x in range(n):
        for y in range(n):
            if data[x][y] == 1:
                answer -= 1
                                                           
    return answer;
