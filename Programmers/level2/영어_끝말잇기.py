def solution(n, words):
    data = [words[0]]
    for i in range(1, len(words)):
        if words[i] in data or words[i][0] != words[i - 1][-1]:
            return [(i % n) + 1, (i // n) + 1]
        else:
            data.append(words[i])
    return [0,0]
