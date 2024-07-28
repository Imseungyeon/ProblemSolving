# set을 이용한 방문 처리, 지나간 좌표가 아닌 길이기 때문에 양방향 처리가 중요

def solution(dirs):
    direction = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}   
    visited = set()
    now_x, now_y = 0, 0
    
    for d in dirs:
        dx, dy = direction[d]
        nx = now_x + dx
        ny = now_y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 양방향 모두 방문 처리
            if (now_x, now_y, nx, ny) not in visited and (nx, ny, now_x, now_y) not in visited:
                visited.add((now_x, now_y, nx, ny))
                visited.add((nx, ny, now_x, now_y))
            now_x, now_y = nx, ny
          
    # 양방 처리로 인해 방문한 길의 2배이기 때문에
    return len(visited) // 2 
