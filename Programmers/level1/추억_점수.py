def solution(name, yearning, photo):
    data = dict(zip(name, yearning))
    answer = []
  
    for p in photo:
        sum = 0
        for person in p:
            if person in data: # photo의 사람이 그리움 목록에 있을 경우에만 더하기
                sum += data[person]
        answer.append(sum)
      
    return answer
