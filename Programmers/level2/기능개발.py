import math

def solution(progresses, speeds):
    answer = []
    temp = [0] * (len(progresses))
    for i in range(len(progresses)):
        temp[i] = math.ceil((100 - progresses[i]) / speeds[i])    
    
    index = 0
    for i in range(len(temp)) :
        if temp[index] < temp[i] :   
            answer.append(i - index) 
            index = i                   
            
    answer.append(len(temp) - index)
    return answer
