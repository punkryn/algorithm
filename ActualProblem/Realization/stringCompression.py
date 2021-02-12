# https://programmers.co.kr/learn/courses/30/lessons/60057
# ababcdcdababcdcd

# 압축 단위를 처음부터 정하고 시작하기 때문에 코드가 짧았던 문제. 실제 정답 코드말고 주석 처리된 코드는 step이 정해져 있지 않고
# 해당 문자열 패턴이 압축할 수 있는 패턴이면 압축을 실행함. 예를 들어 xabab의 경우 정답 코드로는 압축이 안 되지만
# 주석처리된 코드로는 x2ab로 압축이 가능하다. 그 외에는 정답으로 제출한 코드와 깃헙에 올라온 정답 코드의 로직이 거의 같다.

# def solution(s):
#     answer = 0
#
#     length = len(s)
#
#     count = 1
#     result = []
#     sw = 0
#     for i in range(1, length // 2 + 1):
#         tmp = ''
#         pre = 0
#         # for j in range(0, length - i):
#         j = 0
#         count = 1
#         sw = 0
#         while j < length - i:
#             # print(s[j:j + i], s[j + i:j + i + i])
#             #print(j, i)
#             #print(s[j:j + i], s[j + i:j + i + i])
#             if s[j:j + i] == s[j + i:j + i + i]:
#                 pre = count
#                 count += 1
#                 j += i
#                 sw = 1
#             else:
#                 if sw == 1:
#                     tmp += ((str)(count if count != 1 else '') + s[j: j + i])
#                 elif sw == 2:
#                     tmp += ((str)(count if count != 1 else '') + s[j])
#                 # print(tmp)
#
#                 count = 1
#                 if sw == 1:
#                     j += i
#                 elif sw == 2:
#                     j += 1
#                 sw = 2
#         if sw == 1:
#             tmp += ((str)(count if count != 1 else '') + s[j: j + i])
#         elif sw == 2:
#             tmp += s[j:]
#         print(tmp)
#         result.append(len(tmp)) if  len(tmp) > 0 else 1
#     print(result)
#     answer = min(result)
#     return answer

def solution(s):
    answer = 0

    length = len(s)

    result = []

    if length <= 1:
        return length

    for i in range(1, length // 2 + 1):
        tmp = ''
        count = 1
        sw = 0
        for j in range(0, length - i, i):
            # print(s[j:j + i], s[j + i:j + i + i])
            #print(j, i)
            #print(s[j:j + i], s[j + i:j + i + i])
            if s[j:j + i] == s[j + i:j + i + i]:
                count += 1
            else:
                tmp += ((str)(count if count != 1 else '') + s[j: j + i])
                count = 1
                # print(tmp)

        tmp += str(count if count != 1 else '') + s[j + i:]
        print(tmp)
        result.append(len(tmp)) if len(tmp) > 0 else 1
    print(result)
    answer = min(result)
    return answer


s = input()

print(solution(s))