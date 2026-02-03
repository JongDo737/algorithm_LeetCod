def solution(genres, plays):
    answer = []
    # 장르별 노래
    songs_dict = {}
    for genre,play in zip(genres,plays):
        songs_dict[genre] = songs_dict.get(genre,0) + play
    # print(songs_dict)
    
    songs = []
    for i in range(len(genres)):
        songs.append([i,genres[i],plays[i]])
    
    # 1. 장르순
    # 2. 재생순 (내림차순)
    # 3. 고유번호 순(오름차순)
    songs.sort(key=lambda x: (-songs_dict[x[1]], -x[2], x[0] ))
    # print(songs)
    
    genre_count = {}
    for i, genre, play in songs:
        if genre_count.get(genre, 0) < 2:
            answer.append(i)
            genre_count[genre] = genre_count.get(genre,0) +1
        
        # 길이가 넘었거나, 장르가 3개 일 경우
        # if len(answer) > 4 or len(genre_count.keys()) > 3:
        #     answer = answer[:-1]
    
    return answer