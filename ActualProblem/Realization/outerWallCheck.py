from itertools import permutations

def solution(n, weak, dist):
    answer = 0

    dist.sort(reverse=True)
    success = False
    min_value = 100
    # 사람의 수 (1~)
    for i in range(1, len(dist) + 1):
        per = dist[:i]
        # print(per)
        pnum = len(per)

        checklist = [0] * n
        for tmp in weak:
            checklist[tmp] = 1

        starts = permutations(weak, i)
        for asd in starts:
            print(asd, end=' ')
        for pe in starts:
            print(pe)
            checklist = [0] * n
            count = 0
            for tmp in weak:
                checklist[tmp] = 1
            for j, r in enumerate(pe):
                sum = r + per[j]
                for k in range(r, sum + 1):
                    if k < n:
                        checklist[k] += 1
                    else:
                        checklist[(k - n) % n] += 1
            print(checklist)
            for tmp in weak:
                if checklist[tmp] >= 2:
                    count += 1
            if count == len(weak):
                success = True
                return pnum

    return -1


# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

print(solution(n, weak, dist))