from itertools import combinations

mValue = int(1e9)
mci, mcj, mck = [], [], []
for i in range(11):
    for j in range(11):
        for k in range(11):
            if i + j + k == 10:
                job = [32, 51, 55, 14, 20, 64, 11, 33, 20, 64]
                for ci in combinations(job, i):
                    for cii in ci:
                        job.remove(cii)

                    for cj in combinations(job, j):
                        for cjj in cj:
                            job.remove(cjj)

                        for ck in combinations(job, k):
                            m = max(sum(ci), sum(cj), sum(ck))
                            if mValue > m:
                                mValue = m
                                mci, mcj, mck = ci, cj, ck

                        for cjj in cj:
                            job.append(cjj)

                    for cii in ci:
                        job.append(cii)
print(mValue)
print(mci)
print(mcj)
print(mck)