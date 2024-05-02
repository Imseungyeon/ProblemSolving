#우선순위큐 활용

import heapq

def solution(food_times, k):
    answer = -1
    
    if sum(food_times) <= k:
        return answer
    
    num_food = len(food_times)
    q = []
    
    for i in range(num_food):
        heapq.heappush(q, (food_times[i], i + 1))
    
    sum_time = 0
    previous = 0
    
    while sum_time + (q[0][0] - previous) * num_food <= k:
        now = heapq.heappop(q)[0]
        sum_time += (now - previous) * num_food
        num_food -= 1
        previous = now
    
    array = sorted(q, key = lambda x: x[1])
    answer = array[(k - sum_time) % num_food][1]
    return answer
