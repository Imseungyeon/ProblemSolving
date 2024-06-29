def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            if stack and (
                #스택 가장 위의 값과 넣어야 할 값이 짝이라면 pop()
                (stack[-1] == '[' and s[j] == ']') or
                (stack[-1] == '{' and s[j] == '}') or
                (stack[-1] == '(' and s[j] == ')')
            ):
                stack.pop()
            else:
                stack.append(s[j])
                
        if len(stack) == 0:
            answer += 1
        #문자열 회전을 위함
        s.append(s.pop(0))
    return answer
