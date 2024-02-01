def solution(n):
    answer = ''
    while n > 0:
        n, k = divmod(n, 3)
        answer += str(k)
    return int(answer, 3)
