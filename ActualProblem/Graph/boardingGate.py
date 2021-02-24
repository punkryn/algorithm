# 4
# 3
# 4
# 1
# 1


# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4


g = int(input())
p = int(input())

gate = [int(input()) for _ in range(p)]

check = [False] * (g + 1)

count = 0
sw = False
for item in gate:
    while True:
        if not check[item]:
            check[item] = True
            count += 1
            break

        item -= 1

        if item == 0:
            sw = True
            break

    if sw:
        break
print(count)