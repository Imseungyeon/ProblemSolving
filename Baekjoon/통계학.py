# 입력부분 시간 초과 주의
# Counter 함수, 최빈값 구하기 most_common()

from collections import Counter
import sys

# 입력
input = sys.stdin.read
data = input().split()
N = int(data[0])
nums = list(map(int, data[1:]))

# 산술평균
print(round(sum(nums) / N))
# 중앙값
nums.sort()
print(nums[N // 2])
# 최빈값
cnt = Counter(nums).most_common()
if len(cnt) >= 2 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
# 범위
print(nums[-1] - nums[0])
