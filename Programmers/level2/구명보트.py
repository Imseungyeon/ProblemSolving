# 투포인터 사용
# 전체 - (짝 이루는 경우)
def solution(people, limit):
    pair_count = 0
    people.sort()
            
    start = 0
    end = len(people) - 1
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            pair_count += 1
        end -= 1
    return len(people) - pair_count
