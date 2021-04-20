# https://programmers.co.kr/learn/courses/30/lessons/42577

# def solution(phone_book):
#     answer = True
#
#     phone = dict()
#
#     length = len(min(phone_book, key=lambda x: len(x)))
#
#     for pb in phone_book:
#         first = pb[:length]
#         if first in phone.keys():
#             phone[first].append(pb)
#         else:
#             phone[first] = []
#             phone[first].append(pb)
#
#     #print(phone)
#
#     for pb in phone_book:
#         first = pb[:length]
#         for pn in phone[first]:
#             if pb == pn:
#                 continue
#
#             if pb == pn[:len(pb)]:
#                 answer = False
#                 break
#         if not answer:
#             break
#
#     # for a in phone.values():
#     #     if len(a) > 1:
#     #         answer = False
#
#     return answer

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True

#phone_book = ["119", "97674223", "1195524421"]
phone_book = ["119", '1999', '5679', '56789']
print(solution(phone_book))