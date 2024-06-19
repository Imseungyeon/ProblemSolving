# 딕셔너리 활용
def solution(genres, plays):
    answer = []
    data = {}
    gen_dic = {}
    
    # data: 장르별 총 플레이 수, gen_dic: 장르별 (플레이 수, 인덱스)
    for i in range(len(genres)):
        data[genres[i]] = data.get(genres[i], 0) + plays[i]
        gen_dic[genres[i]] = gen_dic.get(genres[i], []) + [(plays[i], i)]
        
    # 총 플레이수 내림차순으로 정렬
    data = sorted(data.items(), key = lambda x: (x[1]), reverse = True)
    
    #플레이 수 내림차순, 인덱스 오름차순으로 정하여 장르별 상위 2개 추가
    for (genre, total) in data:
        gen_dic[genre] = sorted(gen_dic[genre], key = lambda x: (-x[0], x[1]))
        answer += [i for (play, i) in gen_dic[genre][:2]]

    return answer
