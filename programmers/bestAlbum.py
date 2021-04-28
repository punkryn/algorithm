# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    album = dict()

    for i, genre in enumerate(genres):
        if genre not in album.keys():
            album[genre] = []
            album[genre].append(plays[i])
            album[genre].append([plays[i], i])
        else:
            album[genre][0] += plays[i]

            if len(album[genre]) == 2:
                if album[genre][1][0] < plays[i]:
                    album[genre].insert(1, [plays[i], i])
                else:
                    album[genre].append([plays[i], i])
            elif len(album[genre]) > 2:
                if album[genre][1][0] < plays[i]:
                    album[genre].insert(1, [plays[i], i])
                else:
                    if album[genre][2][0] < plays[i]:
                        album[genre].insert(2, [plays[i], i])
                    else:
                        album[genre].append([plays[i], i])

    #print(album)

    album_value = list(album.values())
    album_value.sort(key=lambda x: x[0], reverse=True)
    #print(album_value)

    for value in (album_value):
        for i, v in enumerate(value):
            if i == 0:
                continue

            if i > 2:
                break

            answer.append(v[1])

    return answer

# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))