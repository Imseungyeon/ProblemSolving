#'0b'가 카운트할 때 카운트되는 숫자가 아니므로 bin()함수 사용 가능
#또한 bin() 사용하여 이진수 변환하면 바로 count 함수 사용 가능
def solution(n):
    answer = n
    while(True):
        answer += 1
        if list(format(n, 'b')).count('1') == list(format(answer, 'b')).count('1'):
            return answer
