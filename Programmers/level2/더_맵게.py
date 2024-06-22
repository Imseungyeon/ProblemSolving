# heapq 최소 힙 자동 정렬 이용
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        count += 1
        sco = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, sco)

    return count
  
