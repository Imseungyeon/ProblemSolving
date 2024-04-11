def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(citations[-1], -1, -1):
        count = 0
        for j in range(n):
            if citations[j] >= i:
                count = n - j
                break
        if count >= i:
            answer = max(answer, i)
    return answer
