def solution(t, p):
    p_length = len(p)
    count = 0
    for i in range(0, len(t) - p_length + 1):
        if int(t[i : i + p_length]) <= int(p):
            count += 1
    return count
