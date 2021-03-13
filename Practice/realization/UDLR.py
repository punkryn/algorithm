from sys import stdin

N = int(input())

way = stdin.readline().split()

pos = [1, 1]

for w in way:
    if w == 'U' and pos[0] > 1:
        pos[0] -= 1
    elif w == 'D' and pos[0] < N:
        pos[0] += 1
    elif w == 'L' and pos[1] > 1:
        pos[1] -= 1
    elif w == 'R' and pos[1] < N:
        pos[1] += 1

print(pos[0], pos[1])