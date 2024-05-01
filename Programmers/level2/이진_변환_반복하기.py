def solution(s):
    convert = 0
    zero = 0
    while s != "1":
        convert += 1
        zero += s.count('0')
        s = s.replace("0", "")
        s = bin(len(s))[2:]
    return [convert, zero]
