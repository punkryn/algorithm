# stages = [] 빈 리스트를 전달한 경우 0으로 나누는 에러가 발생한다.
#
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []

    length = len(stages)
    stages.sort()
    pnum = 0
    for i in range(N):
        count = 0
        for j in range(length):
            if (i + 1) == stages[j]:
                count += 1
        print('i, count, length -i', i, count, length - pnum)

        rate = count / (length - pnum)

        pnum += count
        answer.append((i + 1, rate))

    answer.sort(key=lambda x: (-x[1], int(x[0])))
    print(answer)
    tmp = []
    for item in answer:
        tmp.append(item[0])
    return tmp

N=4
#stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages = [1,4,4,4,4]

print(solution(N, stages))