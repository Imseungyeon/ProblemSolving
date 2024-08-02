#RT, CF, JM, AN
def solution(survey, choices):
    answer = ''
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    types = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for i in range(len(survey)):
        choice = choices[i]
        if choice > 4:
            scores[survey[i][1]] += (choice - 4)
        elif choice < 4:
            scores[survey[i][0]] += (4 - choice)
            
    for t1, t2 in types:
        answer += t1 if scores[t1] >= scores[t2] else t2
        
    return answer
