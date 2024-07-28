# 잦은 sum을 사용하기 보다는 현재 다리 위 트럭 무게 추적 변수를 설정하여 업데이트

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    current_weight = 0

    # 다리가 비어있을 때 종료
    while bridge:
        answer += 1
        current_weight -= bridge.popleft()
        # 트럭이 아직 남아있는지 확인
        if trucks:
            if current_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
            
    return answer
