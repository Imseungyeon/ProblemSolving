n = int(input())
count = 0

for i in range(1, n + 1):
    N = []
    while (i > 0):
        N.append(i % 10)
        i //= 10
    if len(N) <= 2:
        count += 1
    else:
        k = N[0] - N[1]
        han_number = True
        for i in range(1, len(N) - 1):
            if (N[i] - N[i + 1]) != k:
                han_number = False
                break
        if han_number:
            count += 1
print(count)
