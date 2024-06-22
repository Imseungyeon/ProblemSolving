# min(len(nums)/2, len(set(num))) set함수 이용시 간단히 해결 가능
def solution(nums):
    data = {}
    for num in nums:
        if num in data:
            data[num] += 1
        else:
            data[num] = 1
    
    return min(len(data), len(nums)/2)
