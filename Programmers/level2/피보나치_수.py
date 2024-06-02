#단순 재귀로 풀면 호출 스택이 커져 런타임 에러 발생
#DP로 해결
def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    
    f = [0] * (n + 1)
    f[1] = 1
    
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 1234567
    return f[n]

def solution(n):
    return fibo(n)
