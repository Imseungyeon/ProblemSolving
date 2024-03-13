def solution(N, stages):
    person = len(stages)               
    failures = []
    
    for i in range(1, N + 1): 
        count = stages.count(i)
        if person == 0:
            failures.append((i, 0))
        else:
            failures.append((i, count / person))
        person -= count
                        
    failures.sort(key = lambda x:x[1], reverse = True)
    
    return [failure[0] for failure in failures]
