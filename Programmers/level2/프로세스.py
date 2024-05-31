# enemerate로 인덱스, 원소 튜플 생성
# 파이썬의 any() 사용해서 더 높은 우선순위가 큐 안에 있는지 확인
from collections import deque

def solution(priorities, location):
    executed = []
    queue = deque((i, j) for i, j in enumerate (priorities))
    
    while queue:
        process = queue.popleft()
        #any(하나라도 있으면) -> True
        if queue and any(process[1] < p[1] for p in queue):
            queue.append(process)
        else:
            executed.append(process)
    
    for a in executed:
        if a[0] == location:
            return executed.index(a) + 1
