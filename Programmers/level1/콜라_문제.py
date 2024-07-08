def solution(a, b, n):
    answer = 0
    while n >= a:
        new_coke = (n // a) * b
        n = new_coke + n % a
        answer += new_coke
    return answer
