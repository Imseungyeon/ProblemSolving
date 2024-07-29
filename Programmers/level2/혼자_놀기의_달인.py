# 방문 처리, BFS 활용하여 해결
# 카드 인덱스는 0부터 시작함을 고려하여 작성

from collections import deque
def solution(cards):
    boxes = []
    visited = [False] * (len(cards) + 1)
    visited[0] = True
    
    for i in range(1, len(visited)):
        if visited[i]: continue
        temp = set([i]) # 중복 방지
        q = deque([i])
        while q:
            now = q.popleft()
            # 이미 방문한 곳이라면 패스
            if visited[now]: continue
            # 방문처리
            visited[now] = True
            temp.add(now)
            q.append(cards[now - 1])
        # 이번 상자에 담은 카드들 갯수   
        boxes.append(len(temp))
        
    boxes.sort(reverse = True)
    if len(boxes) >= 2:
        return boxes[0] * boxes[1]
    else:
        return 0
