from collections import deque

def solution(cards1, cards2, goal):
    deque1 = deque(cards1)
    deque2 = deque(cards2)
    
    for word in goal:
        if deque1 and word == deque1[0]:
            deque1.popleft()
        elif deque2 and word == deque2[0]:
            deque2.popleft()
        else:
            return "No"     
        
    return "Yes"
