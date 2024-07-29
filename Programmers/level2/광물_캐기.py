# lambda 정렬 적절히 활용

def solution(picks, minerals):
    answer = 0
    fatigue = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]
    # 딕셔너리로 각 광물의 레벨이자 인덱스 작성 (다이아: 0, 철: 1, 돌: 2)
    level = {"diamond": 0, "iron": 1, "stone": 2}
    
    # 총 곡괭이로 처리할 수 있는 최대 광물 수 계산
    max_minerals = sum(pick * 5 for pick in picks)

    # 광물을 5개씩 그룹화
    mineral_list = []
    for i in range(0, min(len(minerals), max_minerals), 5):
        mineral_list.append(minerals[i:i+5])

    # 그룹별로 정렬(fatigue[2](돌) 기준으로 정렬해야 우선순위 명확)
    # 피로도가 높은 광물그룹일수록 강한 곡괭이를 사용하여 캐기 위함
    mineral_list = sorted(mineral_list, key=lambda x: -sum(fatigue[2][level[m]] for m in x))
    
    # 피로도 높은 순서로 정렬된 미네랄 그룹 리스트 for문으로 한 그룹씩 처리
    for minerals in mineral_list:
        for i in range(3):
            if picks[i] > 0:
                picks[i] -= 1
                for mineral in minerals:
                    answer += fatigue[i][level[mineral]]
                break

    return answer
