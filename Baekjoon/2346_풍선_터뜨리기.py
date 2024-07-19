# deque 이용해서 rotate
# rotate 방향 -> 양수: 오른쪽으로 회전(시작점은 왼쪽으로 이동해야 함)
# paper_num이 양수인 경우 오른쪽으로 x칸 이동해야 하는데, 이미 popleft되었기 때문에 x-1칸 이동(즉, -(x-1)회전)
# enumerate에서 시작 인덱스 start로 지정 가능
# 리스트 -> 문자열 join함수 ' '.join()하면 사이에 공백 넣기 가능

from collections import deque

N = int(input())
nums = list(map(int, input().split()))
d = deque((i + 1, nums[i]) for i in range(N)) #d = deque((i, n) for i, n in enumerate(nums, start=1))
answer = []

while d:
    idx, paper_num = d.popleft()
    answer.append(idx)
    if not d:
        break
    if paper_num > 0:
        d.rotate(-(paper_num - 1))
    else:
        d.rotate(-paper_num)
print(' '.join(map(str, answer)))
