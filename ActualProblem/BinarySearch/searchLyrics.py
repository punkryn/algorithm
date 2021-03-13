# https://programmers.co.kr/learn/courses/30/lessons/60060

def solution(words, queries):
    answer = []

    words.sort()
    #print(words)

    wordsR = sorted(words, key=lambda k: (k[-1]), reverse=True)


    for query in queries:
        wildindex, wordindex, yesword = wordRel(query)
        if wildindex > wordindex:
            answer.append(search(words, query, wildindex, wordindex, yesword))
        else:
            answer.append(search(wordsR, query, wildindex, wordindex, yesword))

    return answer


def search(words, query, wildindex, wordindex, yesword):
    length = len(words) - 1
    print('words', words)

    first = leftindex(words, query, 0, length)
    if first == None:
        return 0

    second = rightindex(words, query, 0, length)
    print('1first, second', first, second)

    rightPolar = lengthsearch(first, second, len(query), words)
    if rightPolar != None:
        second = rightPolar

    leftPolar = leftlengthsearch(first, second, len(query), words)
    if leftPolar != None:
        first = leftPolar

    #print('2first, second', first, second)
    return second - first + 1

def leftlengthsearch(start, end, goal, words):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or len(words[mid - 1]) < goal) and len(words[mid]) == goal:
        return mid
    elif len(words[mid]) >= goal:
        return leftlengthsearch(start, mid - 1, goal, words)
    else:
        return leftlengthsearch(mid + 1, end, goal, words)

def lengthsearch(start, end, goal, words):
    if start > end:
        return None
    mid = (start + end) // 2
    n = len(words)
    if (mid == n - 1 or len(words[mid + 1]) > goal) and len(words[mid]) == goal:
        return mid
    elif len(words[mid]) > goal:
        return lengthsearch(start, mid - 1, goal, words)
    else:
        return lengthsearch(mid + 1, end, goal, words)

def leftindex(words, query, start, end):
    mid = (start + end) // 2

    if start > end:
        return None

    wildindex, wordindex, yesword = wordRel(query)
    #print('12start, end', start, end)
    #print('12wild, word, word', wildindex, wordindex,yesword)

    if wildindex > wordindex:
        if (mid == 0 or words[mid-1][:wildindex] < yesword) and words[mid][:wildindex] == yesword:
            return mid
        elif words[mid][:wildindex] >= yesword:
            return leftindex(words, query, start, mid - 1)
        else:
            return leftindex(words, query, mid + 1, end)
    else:
        if (mid == 0 or words[mid-1][wordindex:] > yesword or len(words[mid-1][wordindex]) < yesword) and words[mid][wordindex:] == yesword:
            return mid
        elif words[mid][wordindex:] <= yesword:
            return leftindex(words, query, start, mid - 1)
        else:
            return leftindex(words, query, mid + 1, end)

def rightindex(words, query, start, end):
    mid = (start + end) // 2

    if start > end:
        return None

    n = len(words)

    wildindex, wordindex, yesword = wordRel(query)
    print('start, end', start, end)
    print('rightindex wild, word, word', wildindex, wordindex, yesword)


    if wildindex > wordindex:
        if (mid == n - 1 or words[mid + 1][:wildindex] > yesword) and words[mid][:wildindex] == yesword:
            return mid
        elif words[mid][:wildindex] > yesword:
            return rightindex(words, query, start, mid - 1)
        else:
            return rightindex(words, query, mid + 1, end)
    else:
        if (mid == n - 1 or words[mid + 1][wordindex:] < yesword or len(words[mid + 1][wordindex:]) > len(yesword)) and words[mid][wordindex:] == yesword:
            return mid
        elif words[mid][wordindex:] < yesword:
            return rightindex(words, query, start, mid - 1)
        else:
            return rightindex(words, query, mid + 1, end)

def wordRel(query):
    notWord = 0
    for i, word in enumerate(query):
        if word == '?':
            notWord = i
            break

    yesWord = 0
    for i, word in enumerate(query):
        if word != '?':
            yesWord = i
            break

    if yesWord > notWord:
        return notWord, yesWord, query[yesWord:]
    else:
        return notWord, yesWord, query[:notWord]

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# words = ['app', 'apple']
# queries = ['ap?', '?pp']

print(solution(words, queries))