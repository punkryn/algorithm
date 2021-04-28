# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    answer = ''
    players = dict()
    for player in participant:
        if players.get(player):
            players[player] += 1
        else:
            players[player] = 1
    print(players)
    for player in completion:
        if player in players.keys():
            players[player] -= 1

    for key in players.keys():
        if players[key] == 1:
            answer = key

    return answer


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))