def solution(s):
    data = list(s)
    queue = []
    
    for d in data:
        if d == "(":
            queue.append("(")
        else:
            if len(queue) == 0:
                return False
            else:
                queue.pop()
                
    if len(queue) != 0:
        return False
    return True
