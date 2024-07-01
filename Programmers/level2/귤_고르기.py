#파이썬의 Counter 활용
from collections import Counter

def solution(k, tangerine):
    #Counter 활용하여 빈도수 구하기
    tangerine_count = Counter(tangerine)
    tangerine_count = sorted(tangerine_count.values(), reverse=True)

    answer = 0
    counts_sum = 0

    for i in tangerine_count:
        counts_sum += i
        answer += 1
        if counts_sum >= k:
            break
                 
    return answer
