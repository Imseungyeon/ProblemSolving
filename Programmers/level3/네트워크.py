def solution(n, computers):
    visited = [False] * n
    count = 0
    
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if visited[i] == False and computers[v][i]:
                dfs(i)

    for c in range(n):
        if visited[c] == False:
            dfs(c)
            count += 1        
            
    return count
