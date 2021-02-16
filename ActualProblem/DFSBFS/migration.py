import sys
sys.setrecursionlimit(100000)

n, l, r = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#print(land)
total = 0
def mig():
    global total
    line = []
    for i in range(n):
        line.append([])
        for j in range(n):
            line[i].append([False, False, False, False])

    count = 0
    #tmp = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            #tmp[i][j] = True
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if not (0 <= ni < n and 0 <= nj < n):
                    continue

                #print(land[i][j], land[ni][nj])
                if l <= abs(land[i][j] - land[ni][nj]) <= r:
                    #print(i, j, k)
                    line[i][j][k] = True
                    #print(line)
                else:
                    count += 1
            #print(line)
    #print(line)
    #print(count)
    if (count // 2) == (n * (n - 1) * 2):
        return

    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            union = [(i, j)]
            dfs((i, j), land, line, visited, union, 1)
            #print(i, j, union)
            result = 0
            countryNum = len(union)
            for country in union:
                cx, cy = country
                result += land[cx][cy]

            if len(union) > 1:
                result //= countryNum

            for country in union:
                cx, cy = country
                land[cx][cy] = result
    #print(land)
    total += 1
    mig()


def dfs(start, land, line, visited, union, count):
    x, y = start

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue

        if visited[nx][ny]:
            continue

        #print(nx, ny, i)
        if line[x][y][i]:
            union.append((nx, ny))
            #print(union)
            dfs((nx, ny), land, line, visited, union, count + 1)

mig()
print(total)