def solution(s):
    s = s[2:-2]
    l = s.split("},{")
  
    #길이 짧은 것 순서로 sort
    l.sort(key=len)
  
    #새로 추가되는 수 answer에 추가
    answer = [int(l[0])]
    for i in range(1, len(l)):
        temp = list(map(int, l[i].split(",")))
        for t in temp:
            if t not in answer:
                answer.append(t)
              
    return answer
