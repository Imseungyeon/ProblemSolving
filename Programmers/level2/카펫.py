#완전탐색 for문 범위 최소화

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for height in range(1, int(total ** 0.5) + 1):
        if total % height == 0:
            width = int(total / height)
            if (width - 2) * (height - 2) == yellow:
                answer = [width, height]
                break
    
    return answer
