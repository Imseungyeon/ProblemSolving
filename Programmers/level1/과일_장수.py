def solution(k, m, score):
    answer = 0
    score.sort()
    # 판매하지 않을 남는 사과 제외한 리스트
    score = score[len(score) % m:]
    for i in range(0, len(score), m):
        answer += score[i] * m   
    return answer
