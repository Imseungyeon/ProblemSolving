# 문자 리스트 -> 정수 리스트 : map(int, 리스트명)

full = input()

remove_minus = full.split('-')
result = sum(map(int, remove_minus[0].split('+')))
for i in range(1, len(remove_minus)):
    result -= sum(map(int, remove_minus[i].split('+')))
    
print(result)
