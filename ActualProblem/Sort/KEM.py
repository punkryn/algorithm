# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

# https://www.acmicpc.net/problem/10825

n = int(input())

score = []
for _ in range(n):
    score.append(list(input().split()))

for s in score:
    for i in range(1, 4):
        s[i] = int(s[i])

# score.sort(key=lambda k: k[0])
# score.sort(key=lambda k: k[3], reverse=True)
# score.sort(key=lambda k: k[2])
# score.sort(key=lambda k: k[1], reverse=True)

score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(score[i][0])