def solution(n, lost, reserve):
    l = set(lost) - set(reserve)
    r = set(reserve) - set(lost)
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    
    return n - len(l)
