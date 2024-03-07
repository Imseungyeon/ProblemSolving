from itertools import combinations

def solution(number):
    count = 0
    data = list(combinations(number, 3))
    for x in data:
        if sum(x) == 0:
            count += 1
    return count
