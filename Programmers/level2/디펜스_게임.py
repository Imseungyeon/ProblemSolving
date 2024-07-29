import heapq

def solution(n, k, enemy):
    # 힙을 사용하여 가장 병력 소모가 큰 적부터 제거
    max_heap = []
    total_enemy = 0

    for i in range(len(enemy)):
        # 적을 힙에 추가 : 음수로 저장하여 최대 힙 구현
        heapq.heappush(max_heap, -enemy[i])
        total_enemy += enemy[i]

        # 병사가 부족할 때
        if total_enemy > n:
            # 더 이상 스킬을 사용할 수 없으면 라운드 반환하며 종료
            if k == 0:
                return i
            # 병사 많던 라운드에 스킬 사용
            total_enemy += heapq.heappop(max_heap)
            k -= 1

    # 모든 라운드를 버틸 수 있으면 전체 라운드 수 반환
    return len(enemy)

