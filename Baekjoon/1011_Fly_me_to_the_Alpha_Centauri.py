T = int(input())
answer = []

for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    
    if distance == 0:
        answer.append(0)
        continue
    
    k = 1
    while k * k < distance:
        k += 1
    if k * (k - 1) >= distance:
        answer.append(2 * k - 2)
    else:
        answer.append(2 * k - 1)

print(' '.join(map(str, answer)))
            
    
