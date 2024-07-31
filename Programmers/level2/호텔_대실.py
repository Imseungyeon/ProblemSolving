# for문 돌리기 -> 데이터 1000개이므로 충분
# times 오름차순 정렬
# max로 최소 필요 객실의 수 구하기

def solution(book_time):
    times = []
    for new_book in book_time:
        start_time = int(new_book[0].replace(':', ''))
        end_time = int(new_book[1].replace(':', '')) + 10
        
        # 9:50이라면 9:60이 아닌 10:00으로 표현하기 위함
        if end_time % 100 >= 60:
            end_time = (end_time // 100 + 1) * 100 + (end_time % 100 - 60)
        
        times.append((start_time, 'start'))
        times.append((end_time, 'end'))
    
    times.sort()
    
    room = 0
    answer = 0
    
    for time, type in times:
        if type == 'start':
            room += 1
        else:
            room -= 1
        # 방 필요 갯수 상태 저장
        answer = max(answer, room)
    return answer
