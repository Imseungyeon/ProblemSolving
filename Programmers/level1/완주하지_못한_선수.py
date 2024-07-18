# 풀이 1과 2 모두 시간 복잡도는 O(n)이지만, 2(Counter 활용)의 경우 코드가 간결하고 파이썬 내장 라이브러리를 사용하여 최적화되어 있음

# 풀이 1. 시간 초과 방지를 위해 set으로 동명이인의 경우를 제외하고 처리, 동명이인의 경우만 key-value로 해결
def solution(participant, completion):
  
    def to_dict(dic, players):
        for player in players:
            if player not in dic: dic[player] = 1
            else: dic[player] += 1
        return dic
            
    p, c = set(participant), set(completion)
    incompletion = set(participant) - set(completion)
    
    if len(incompletion) == 1: return list(incompletion)[0]
    else:
        dic_p, dic_c = {}, {}
        dic_p = to_dict(dic_p, participant)
        dic_c = to_dict(dic_c, completion)
        for player in dic_p:
            if dic_p[player] != dic_c[player]: return player
        
# 풀이 2. Counter 활용
from collections import Counter

def solution(participant, completion):

    count_p = Counter(participant)
    count_c = Counter(completion)

    incomplete = count_p - count_c # 빠진 선수 찾기
    return list(incomplete.keys())[0]


            
