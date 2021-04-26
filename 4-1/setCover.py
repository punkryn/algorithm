def set_cover(universe, subsets):
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != universe:
        subset = max(subsets, key=lambda s: len(s-covered))
        cover.append(subset)
        covered |= subset
    return cover

universe = set(range(6))
subsets = [set([0, 3, 4]),
           set([1, 2, 3]),
           set([2, 3, 4]),
           set([0, 4, 5]),
           set([1, 4, 5]),
           set([2, 4, 5])
           ]
cover = set_cover(universe, subsets)
print(cover)







