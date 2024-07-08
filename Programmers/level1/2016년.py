def solution(a, b):
    week_day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for i in range(a - 1):
        days += month_day[i]
    answer = week_day[(days + b - 1) % 7]
    return answer
