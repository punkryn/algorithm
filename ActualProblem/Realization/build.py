# 설치 조건
# 1. 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 2. 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# 삭제 조건
# 삭제를 할 수 있다는 것은 해당 구조물이 없어도 이 구조물에 영향을 받는 좌표에서 구조물을 설치할 수 있다는 뜻이다.
# 따라서 재귀함수로 해당 좌표에서 삭제하고자 하는 구조물을 지운 상태에서
# 구조물을 설치할 수 있는지 검사하여 설치할 수 있다면 삭제할 수 있다는 뜻이다.
# 기둥일 경우 삭제 조건은 기둥에 해당하는 좌표에서 한 칸 위에서 영향받는 경우 세 가지를 검사한다.
# 좌상에서 보, 상에서 기둥과 보
# 보일 경우 보의 양 끝에서 영향을 받는 네 가지 좌표에 대해 검사를 한다.
# 좌측에서 영향받는 보와 기둥을 검사하고 우측에서 영향 받는 보와 기둥을 검사하면 네 가지가 된다.

# 정답을 보고나서
# 일단 삭제하거나 설치를 해보고 조건을 검사한다. 조건을 검사하여 불가능하면 다시 원래대로 돌린다.
# 배열을 수정하지 않고 정답 리스트에 해당 위치의 보나 기둥이 있다면 조건 검사를 충분히 수행할 수 있다. <--- 코드가 훨씬 간결해짐
# 즉 조건 검사를 할 때 인덱스 값을 조절하는 게 아니라 좌표가 정답 리스트 안을 체크함으로써 조건 검사를 진행한다

def solution(n, build_frame):
    answer = []

    #room = [[[0, 0]] * (n + 1) for _ in range(n + 1)]
    room = []
    for i in range(n + 1):
        for j in range(n + 1):
            room.append([])
            room[j].append([0, 0])
    #print(room)

    for step in build_frame:
        x, y, a, b = step
        x_ = n - y
        y_ = x
        if condition_check([x_, y_, a, b], room, n):
            if b == 1:
                room[x_][y_][a] = 1
                answer.append([x, y, a])
            elif b == 0:
                room[x_][y_][a] = 0
                print(x_, y_, a)
                answer.remove([x, y, a])

    answer.sort(key=lambda k:k[2])
    answer.sort(key=lambda k:k[1])
    answer.sort(key=lambda k:k[0])
    return answer

def condition_check(step, room, n):
    # a: 0 기둥 1 보 b: 0 삭제 1 설치
    x, y, a, b = step
    x_ = x
    y_ = y
    #tmp = x
    #x = n - y
    #y = tmp
    print('x, y', x, y, a, b)
    for i in range(n + 1):
        for j in range(n + 1):
            print(room[i][j], end=' ')
        print()
    print()
    if b == 1:
        # 기둥일 때
        if a == 0:
            # 조건
            if (x == n) or ((y - 1 >= 0 and room[x][y - 1][1] == 1) or (y + 1 <= n and room[x][y][1] == 1)) or (x + 1 <= n and room[x + 1][y][0] == 1):
                # 조건을 만족할 때 설치
                #room[x][y][0] = 1
                #print(room)
                print('x, y', x, y, a)
                return True

        # 보일 때
        elif a == 1:
            #print(room[x + 1][y][0])
            if ((x + 1 <= n and room[x + 1][y][0] == 1) or (x + 1 <= n and room[x + 1][y + 1][0] == 1)) or ((y - 1 >= 0 and room[x][y - 1][1] == 1) and (y + 1 <= n and room[x][y + 1][1] == 1)):
                #room[x][y][1] = 1
                print('x, y', x, y, a)
                return True

    elif b == 0:
        if a == 0:
            # 한 칸 위에 기둥이 없어야하고, 좌우로 보가 있을 때 기둥을 삭제해도 보가 유지될 수 있어야 한다.
            # 한 칸 위에 기둥이 있더라도 보가 있으면 삭제할 수 있다.
            # if room[x - 1][y][0] == 0 or (room[x - 1][y][0] == 1 and (room[x - 1][y - 1][1] == 1 or room[x - 1][y][1] == 1)):
            #     room[x][y][0] = 0

            # if condition_check([x - 1, y, 1, 1], room, n) and condition_check([x - 1, y - 1, 1, 1], room, n):
            #     return True
            for i in range(n + 1):
                for j in range(n + 1):
                    print(room[i][j], end=' ')
                print()
            print()
            if x - 1 >= 0 and room[x - 1][y][0] == 1:
                room[x][y][0] = 0
                if not condition_check([x - 1, y, 0, 1], room, n):
                    room[x][y][0] = 1
                    return False
                room[x][y][0] = 1
            if x - 1 >= 0 and room[x - 1][y][1] == 1:
                room[x][y][0] = 0
                if not condition_check([x - 1, y, 1, 1], room, n):
                    room[x][y][0] = 1
                    return False
                room[x][y][0] = 1
            if x - 1 >= 0 and y - 1 >= 0 and room[x - 1][y - 1][1] == 1:
                room[x][y][0] = 0
                if not condition_check([x - 1, y - 1, 1, 1], room, n):
                    room[x][y][0] = 1
                    return False
                room[x][y][0] = 1
            return True

        elif a == 1:
            # 보의 양 끝에 기둥이 없어야한다.

            # if (room[x][y][0] == 0 or (room[x][y][0] == 1 and room[x + 1][y][0] == 1)) and room[x][y - 1][0] == 0:
            if room[x][y][0] == 1:
                room[x][y][1] = 0
                if not condition_check([x, y, 0, 1], room, n):
                    room[x][y][1] = 1
                    return False
                room[x][y][1] = 1

            if y - 1 >= 0 and room[x][y - 1][1] == 1:
                room[x][y][1] = 0
                if not condition_check([x, y - 1, 1, 1], room, n):
                    room[x][y][1] = 1
                    return False
                room[x][y][1] = 1

            if y + 1 <= n and room[x][y + 1][0] == 1:
                room[x][y][1] = 0
                if not condition_check([x, y + 1, 0, 1], room, n):
                    room[x][y][1] = 1
                    return False
                room[x][y][1] = 1

            if y + 1 <= n and room[x][y + 1][1] == 1:
                room[x][y][1] = 0
                if not condition_check([x, y + 1, 1, 1], room, n):
                    room[x][y][1] = 1
                    return False
                room[x][y][1] = 1
            return True
    return False

n = 5
#build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
#build_frame = [[5, 0, 0, 1], [5, 1, 0, 1]]
build_frame = [[3,0,0,1],[2,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1],[2,1,1,0]]

print(solution(n, build_frame))