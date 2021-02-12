# https://programmers.co.kr/learn/courses/30/lessons/60062

# 원과 같이 인덱스를 탐색할 때 인덱스가 다시 0으로 돌아오는 경우 그대로 계산을 하면 상당히 까다롭다.
# 따라서 원을 일자 형태로 펴서 길이를 2배로 하면 인덱스를 다시 0으로 돌리는 번거로움이 없다.
# 시작은 weak의 각 지점의 인덱스로 한다. 따라서 weak리스트의 길이만큼 반복하며 시작지점을 정한다. (여기서는 0 ~ 4)
# 친구 리스트와 이 리스트의 길이만큼 순열을 만들어 각각의 경우를 반복한다. 나는 weak를 순열로 만들었는데 이렇게 하면
# 경우가 굉장히 많아진다. weak의 시작점만 반복문으로 정하고 친구 리스트를 순열로 만들어 경우를 줄인다. 순열로 만들 때
# 리스트의 길이만큼 순열로 만드는 이유는 친구들의 순서의 조합 방식을 정하는 것이다. 즉 시작지점은 같아도 누가 먼저 시작
# 하느냐에 따라 다르기 때문에 조합으로 만드는 것이다. 이렇게 순서를 정하고 이제 몇 명이 필요한지만 알면 된다.

# 투입할 친구의 수를 1로 초기화하고 시작지점에서 처음 친구를 투입했을 때 이동할 수 있는 위치까지 이동한 뒤
# position을 초기화한다. 이제 시작지점부터 시작해서 weak의 위치를 돌며 이동한 친구가 어디까지 이동하였는지
# 확인한다. 이 때 weak의 어떤 지점보다 값이 작으면 그 위치에 도달하지 못 한 것이기 때문에 친구를 한 명 더 투입한다.
# 따라서 count를 1 높이고 도달하지 못 한 weak 지점에서 다음 친구가 이동할 수 있는 곳까지 이동하여 position을 변경한다.
# 만약 count가 투입할 수 있는 친구의 수보다 높아지면 이는 모든 weak 지점을 방문할 수 없는 것이기 때문에 -1을 return한다.
#

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        print('start', start)
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            print('friends', friends)
            count = 1 # 투입할 친구의 수
            print('count', count)
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            print('pos', position)
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                print('index', index, 'weak[index]', weak[index])
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    print('count', count, )
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        print('end')
                        break
                    position = weak[index] + friends[count - 1]
                    print('pos2', position)
            answer = min(answer, count) # 최솟값 계산
            print('ans', answer)
    if answer > len(dist):
        return -1
    return answer

n = 12
#weak = [1, 5, 6, 10]
#dist = [1,2,3,4]

weak = [1,3,4,9,10]
dist = [3,5,7]
print(solution(n, weak, dist))