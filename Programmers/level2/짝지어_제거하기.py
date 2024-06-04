# 스택의 성질 이용하여 해결
# 인덱스 [-1] 이용하여 pop()을 대신하여 데이터 변경없이 비교연산 가능
def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return 0
    else:
        return 1
