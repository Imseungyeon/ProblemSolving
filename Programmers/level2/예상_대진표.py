def solution(n,a,b):
    count = 0
    #2로 나눴을 때 몫이 같으면 됨
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2 # //를 사용하여 1 더할지 여부 결정과정 생략 가능
        count += 1
    return count
