# 정규표현식 적절히 사용하기
import re

def solution(new_id): 
    # 1단계
    answer = new_id.lower()
    # 2단계
    # 소문자, 숫자, -, _, . 제외하고 모두 삭제
    answer = re.sub(r"[^a-z0-9-_.]", "", answer)
    # 3단계 
    # .이 두 개 이상 연속하면 . 한 개 제외하고 모두 삭제
    answer = re.sub(r"\.{2,}", ".", answer)
    # 4단계
    if len(answer) > 0 and answer[0] == '.': 
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.': 
        answer = answer[:-1]
    # 5단계
    if answer == "": answer = "a"
    # 6단계
    if len(answer) >= 16: 
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]
    #7단계
    while len(answer) <= 2:
        answer += answer[-1]
    return answer
