# 순열 풀이법 (dfs풀이도 가능)
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for perm in permutations(dungeons):
        temp_k = k
        count = 0
        for min_k, use_k in perm:
            if temp_k >= min_k:
                temp_k -= use_k
                count += 1
            else:
                break
        answer = max(answer, count)
        
    return answer
