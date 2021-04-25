# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()
    num = []
    for i in range(max(citations)+1):
        ct = 0
        for val in citations:
            if val >= i:
                ct = ct+1
            else:
                ct = ct+0
        num.append(ct)
        print(num)
        if num[i] >= i:
            answer = i
        else:
            break

    return answer

citations = [3, 0, 6, 1, 5, 4, 100]
print(solution(citations))