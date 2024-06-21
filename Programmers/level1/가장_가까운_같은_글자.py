#딕셔너리 이용하여 특정 글자의 마지막 인덱스 저장
def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer
