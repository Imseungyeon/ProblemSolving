#deque로 구현
#형 변환 주의
from collections import deque

def solution(operations):
    temp = []
    operations_queue = deque(operations)
    
    while operations_queue:
        operation = operations_queue.popleft()
        if operation[0] == "I":
            temp.append(int(operation[2:]))
        else:
            if len(temp) == 0: continue
            if int(operation[2:]) == 1:
                temp.remove(max(temp))
            else:
                temp.remove(min(temp))
    
    if len(temp) == 0: return [0,0]
    return [max(temp), min(temp)]
