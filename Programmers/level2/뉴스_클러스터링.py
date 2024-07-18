# J(A, B) = 교집합의 크기 / 합집합의 크기
# A, B 모두 공집합이면 J(A, B) = 1

# upper 해서 대/소문자 구분 없애기
# dic에 두 글자씩 넣으면서(모두 문자인지 체크) 이미 있는 key면 value += 1 없으면 value = 1

# 교집합: dic1 순회하며 다른 dic에 있으면 value 더 작은 쪽 (min 사용)
# 합집합: dic2 순회하며 다른 dic에 있으면: value 더 큰 쪽 (max 사용) 
#                             없으면: 값 그냥 더하기
#       dic2 순회하며 dic1에 있으면 넘어가고 없는 것 더하기

def solution(str1, str2):
    
    def to_dict(dic, str):
        for i in range(len(str) - 1):
            s = str[i: i + 2]
            if s.isalpha():
                if s in dic: dic[s] += 1
                else: dic[s] = 1
        return dic
    
    dic1, dic2 = {}, {}
    dic1 = to_dict(dic1, str1.upper())
    dic2 = to_dict(dic2, str2.upper())
    
    inter, union = 0, 0 #교집합, 합집합
    
    for str in dic1:
        if str in dic2:
            inter += min(dic1[str], dic2[str])
            union += max(dic1[str], dic2[str])
        else: union += dic1[str]
    
    for str in dic2:
        if str not in dic1:
            union += dic2[str]
    
    if union == 0: return 65536 
    else:
        return int((inter / union) * 65536)
