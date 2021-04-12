import heapq

def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    print(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        print(heap)

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

frequency = {'A': 450, 'T': 90, 'G': 120, 'C': 270}
huff = encode(frequency)
print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff:
    print(p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])