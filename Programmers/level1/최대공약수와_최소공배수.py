def solution(n, m):
    answer = [gcd(n, m), lcd(n, m)]
    return answer

def gcd(n, m):
    value = 1
    for i in range(min(n, m), 0, -1):
        if (n % i == 0) and (m % i == 0):
            value = i
            break
    return value
        
def lcd(n, m):
    value = n * m
    for i in range(max(n, m), n * m + 1):
        if i % n == 0 and i % m == 0:
            value = i
            break
    return value
