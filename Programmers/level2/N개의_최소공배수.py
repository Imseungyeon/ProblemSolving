#from fractions import gcd 활용하지 않고 구현

def lcm(a, b):
    i = 1
    while True:
        n = b * i
        if n % a == 0:
            return n
        i += 1

def solution(arr):
    answer = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        answer = lcm(answer, arr[i])
    return answer
