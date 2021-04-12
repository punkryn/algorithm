import heapq

class Node:
    def __init__(self, data, word, left, right):
        self.data = data
        self.word = word
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.data < other.data

def makeWordFreqDic(sentence):
    d = dict()
    for word in sentence:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d

def makeNode(nodelist):
    node = []
    for item in nodelist.keys():
        node.append(Node(nodelist[item], item, None, None))
    return node

def huffmantree(node):
    if len(node) == 1:
        return node
    else:
        min1 = heapq.heappop(node)
        min2 = heapq.heappop(node)
        heapq.heappush(node, [min1[0] + min2[0], Node(min1[1].data + min2[1].data, ' ', min1[1], min2[1])])
        huffmantree(node)
        return node

def round(node, buf, binary):
    if(node.left == None):
        #print(node.word, end=' ')
        #print(buf)
        binary[node.word] = ''.join(buf)
        return
    else:
        buf.append('0')
        round(node.left, buf, binary)
        buf.pop()
        buf.append('1')
        round(node.right, buf, binary)
        buf.pop()

def stob(s, binary):
    bits = ''
    for word in s:
        bits += binary[word]
    return bits

def decode(tree, bits, buf, i):
    if tree.left == None:
        buf.append(tree.word)
        return i
    else:
        if bits[i] == '0':
            return decode(tree.left, bits, buf, i + 1)
        else:
            return decode(tree.right, bits, buf, i + 1)


s = "add fasd dfa aas dd fd saad fasf aas fdd dfaas df dfff sdgg fsgsas"
freq = makeWordFreqDic(s.replace(' ', ''))
print(freq, end='\n\n')
nodelist = makeNode(freq)
heap = []
for node in nodelist:
    heap.append([node.data, node])

heapq.heapify(heap)
#print(heap)

heap = huffmantree(heap)
print(heap, end='\n\n')

binary = dict()
round(heap[0][1], [], binary)
print(binary, end='\n\n')

compress = 0
for word, bits in binary.items():
    compress += freq[word] * len(bits)

length = len(s.replace(' ', ''))
print("압축률:", str((compress / (len(binary.keys()) * length * 8)) * 100) + '%')

bits = stob(s.replace(' ', ''), binary)
print(bits, end='\n\n')


buf = []

index = 0
while index < len(bits):
    index = decode(heap[0][1], bits, buf, index)

print(buf)
print(''.join(buf))