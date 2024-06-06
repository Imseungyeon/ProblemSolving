#해시맵 사용하여 구현
#딕셔너리의 get(key, x) -> key가 없는 경우 x를 리턴

def solution(clothes):
    hash = {}
    for name, type in clothes:
        hash[type] = hash.get(type, 0) + 1
    
    answer = 1
    for type in hash:
        answer *= (hash[type] + 1)
        
    return answer - 1
