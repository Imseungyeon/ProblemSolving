def solution(answers):
    correct = [0, 0, 0, 0]
    
    second = [2, 1, 2, 3, 2, 4, 2, 5] 
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    
    for i in range(len(answers)):
        if answers[i] == (i % 5) + 1:
            correct[1] += 1
        if answers[i] == second[i % len(second)]:
            correct[2] += 1
        if answers[i] == third[i % len(third)]:
            correct[3] += 1
            
    answer = []
    maxvalue = max(correct)
    for i in range(1, len(correct)):
        if maxvalue == correct[i]:
            answer.append(i)
    return answer
