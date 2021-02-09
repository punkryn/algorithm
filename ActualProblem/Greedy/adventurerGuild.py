# 공포도가 높은 모험가부터 그룹을 구성한다. 이유는 최대한 많은 그룹을 만드려면 공포도가 낮은 사람들은
# 적은 인원으로 그룹을 구성할 수 있기 때문에 공포도가 높은 인원을 최대한 같은 그룹에 넣어서
# 공포도가 낮은 모험가를 덜 끌어들이는 것이 좋기 때문이다.
# 따라서 공포도를 내림차순 정렬하여 낮은 인덱스부터 그룹을 만든다.

# 5
# 2 3 1 2 2

# 6
# 2 3 2 3 2 2

# 5
# 3 3 3 3 1

# 5
# 3 3 3 3 3

# 6
# 3 3 3 4 1 1

# n = int(input())
#
# tmp = map(int, input().split())
# fear = []
# for i in tmp:
#     fear.append(i)
#
# fear.sort(reverse=True)
# print(fear)
#
# index = 0
# count = 0
# while index < n:
#     print(index)
#     if index + fear[index] < n:
#         index += fear[index]
#         count += 1
#     elif index + fear[index] == n:
#         count += 1
#         break
#     else:
#         if index + 1 < n:
#             index += 1
#         elif index + 1 == n:
#             if fear[index] == 1:
#                 count += 1
#                 break
#             else:
#                 break
#
#
# print(count)


n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    print('count', count, i)
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        print('result', result)
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력