from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    want_dict = dict(zip(want, number))
    
    for i in range(len(discount) - 9):
        discount10 = discount[i : i + 10]
        discount_counter = Counter(discount10)
        
        # want_dict의 모든 아이템에 대해 discount_counter에 그 수의 이상이 들어있을 때
        if all(discount_counter.get(item, 0) >= want_dict[item] for item in want_dict):
            answer += 1
    
    return answer
