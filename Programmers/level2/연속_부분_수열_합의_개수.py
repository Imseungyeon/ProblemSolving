# 풀이 1. 인덱스 범위 문제를 해결하기 위해 elements의 길이를 두 배로 늘려 계산
# 정답이긴 하나 시간이 매우 오래 걸림
def solution(elements):
    sums = set()
    len_elements = len(elements)
    
    elements = elements * 2
    for i in range(len_elements):
        for j in range(len_elements):
            sums.add(sum(elements[j: j + i + 1]))
            
    return len(sums)

# 풀이 2. 슬라이딩 윈도우 기법 사용
def solution(elements):
    sums = set()
    len_elements = len(elements)
    
    for length in range(1, len_elements + 1):  # 부분 수열의 길이
        current_sum = sum(elements[:length])
        sums.add(current_sum)
        
        for start in range(1, len_elements):  # 시작 인덱스
            # 윈도우가 이동할 때마다 맨 앞의 시작 요소 빼고, 새롭게 맨 뒤 요소 추가
            # 원형 리스트이기 때문에 %len_elements 이용
            current_sum = current_sum - elements[start - 1] + elements[(start + length - 1) % len_elements]
            sums.add(current_sum)
    
    return len(sums)
