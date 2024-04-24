def solution(s, n):
    spell = list(s)

    for i in range(len(spell)):
        if spell[i].isalpha():
            if spell[i].islower():
                spell[i] = chr(ord('a') + ((ord(spell[i]) - ord('a') + n) % 26))
            else:
                spell[i] = chr(ord('A') + ((ord(spell[i]) - ord('A') + n) % 26))
    answer = ''.join(spell)
    return answer
