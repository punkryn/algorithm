# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 0

    kind = dict()

    for cloth in clothes:
        name, kind_of_cloth = cloth
        if kind_of_cloth in kind.keys():
            kind[kind_of_cloth].append(name)
        else:
            kind[kind_of_cloth] = []
            kind[kind_of_cloth].append(name)

    print(kind)

    result = 1
    for value in kind.values():
        result *= (len(value) + 1)

    answer = result - 1

    return answer

#clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))