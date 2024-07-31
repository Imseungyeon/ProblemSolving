# 조건을 명확히 나누는 것이 중요
# deque 생성시 deque(range(a, b))로 생성 가능
from collections import deque

def solution(order):
    answer = 0
    stack = []
    container = deque(range(1, len(order) + 1))
    order = deque(order)
    
    while container or stack:
        if stack and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer += 1
        elif container and container[0] == order[0]:
            order.popleft()
            container.popleft()
            answer += 1
        elif container:
            stack.append(container.popleft())
        else:
            break
                        
    return answer
