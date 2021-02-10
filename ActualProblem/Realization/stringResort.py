# K1KA5CB7

s = input()

tmp = []
for i in s:
    tmp.append(i)

tmp.sort()
# print(tmp)

result = 0
sentence = ''
for i, word in enumerate(tmp):
    if tmp[i].isdigit():
        result += int(word)
    else:
        sentence += word

print(sentence + str(result))