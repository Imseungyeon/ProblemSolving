# heapq 최소 힙(Min Heap) 자동 정렬 이용
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

# 매번 전체 정렬을 필요로 하는 deque 활용시 효율성 떨어짐
from collections import deque

def solution(scoville, K):
    q = deque(sorted(scoville))
    count = 0
    while q and q[0] < K:
        if len(q) < 2:
            return -1
        count += 1
        
        sco = q.popleft() + q.popleft() * 2
        q.append(sco)
        q = deque(sorted(q)) 

    return count
  
