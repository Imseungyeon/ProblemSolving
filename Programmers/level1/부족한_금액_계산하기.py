def solution(price, money, count):
    change = money - price * (count * (count + 1) / 2)
    if change < 0:
        return (-1) * change
    else:
        return 0
