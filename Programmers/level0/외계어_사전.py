def solution(spell, dic):
    answer = 1
    count = len(dic)
    
    for word in dic:
        for s in spell:
            if s not in word:
                count -= 1
                break

    if count != 1:
        answer = 2
                      
    return answer
