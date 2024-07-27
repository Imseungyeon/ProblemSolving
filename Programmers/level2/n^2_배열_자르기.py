# 배열을 생성하지 않고(2차원, 1차원 모두) 필요한 값만을 구해내야 시간 단축

def solution(n, left, right):
    answer = []    
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        answer.append(max(row + 1, col + 1))
    return answer
