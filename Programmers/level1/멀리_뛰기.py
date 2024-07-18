# 재귀로 풀면 매우 비효율적이므로 시간 초과, 따라서 dp로 풀어야 함
# dp[n] = dp[n - 1] + dp[n - 2]

def solution(n):
    if n == 1: return 1
    if n == 2: return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567 
        
    return dp[n]
    
    
    
    
