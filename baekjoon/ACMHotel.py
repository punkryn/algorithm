# https://www.acmicpc.net/problem/10250

# 2
# 6 12 1
# 30 50 72

for _ in range(int(input())):
    h, w, n = map(int, input().split())

    level = str(n % (h))
    if level == '0':
        level = str(h)

    if n % h == 0:
        room = str(n // h)
    else:
        room = str(n // h + 1)
    if len(room) < 2:
        room = ('0' + room)

    print(level+room)