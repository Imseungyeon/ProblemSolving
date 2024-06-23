# 효율성 테스트 실패ver.
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer
    while n > 0: 
        n -= 1
        works.sort(reverse = True)
        for i in range(len(works)):
            if  works[i] >= (sum(works) / len(works)):
                works[i] -= 1
                break
                
    for work in works:
        answer += work * work
    return answer

# 최종ver.
# 정렬에서 많은 시간이 소요되므로 최대 힙을 이용하여 자동 정렬되도록
import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return answer
    
    # 음수로 변환해서 최대 힙으로 만들기
    works = [-work for work in works]
    heapq.heapify(works)
    
    for _ in range(n):
        num = heapq.heappop(works) + 1 # 음수 값이니까 1 더하기
        heapq.heappush(works, num)
                       
    for work in works:
        answer += work * work # 제곱의 합이므로 음수 -> 양수 처리과정 생략 가능
    return answer
