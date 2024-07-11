# heapq로 우선순위큐 구현
import heapq

def solution(k, score):
    answer = []
    fames = []
    for s in score:
        heapq.heappush(fames, s)
        if len(fames) > k:
            heapq.heappop(fames)
        answer.append(fames[0])
        
    return answer
