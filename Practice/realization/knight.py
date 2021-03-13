pos = input()

col = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#print(col.index(pos[0]))
x = int(pos[1])
y = col.index(pos[0])

# UDLR
dy = [0, 0, -2, 2]
dx = [-2, 2, 0, 0]

ly = [[-1, 1], [-1, 1], [0, 0], [0, 0]]
lx = [[0, 0], [0, 0], [-1, 1], [-1, 1]]

count = 0
for i in range(4):
    xpos = x
    ypos = y

    xpos += dx[i]
    ypos += dy[i]

    for j in range(2):
        ypos += ly[i][j]
        xpos += lx[i][j]

        if xpos < 1 or xpos > 8 or ypos < 1 or ypos > 8:
            ypos -= ly[i][j]
            xpos -= lx[i][j]
            continue
        print(xpos, ypos)
        ypos -= ly[i][j]
        xpos -= lx[i][j]
        count += 1

print(count)