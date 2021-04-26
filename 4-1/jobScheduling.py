# def jobScheduling(jobs):
#     schedule = []
#     noMachine = 0
#     L = sorted(jobs)
#     while L:
#         task = L.pop(0)
#         found = False
#         for mi in schedule:
#             if mi[1] <= task[0]:
#                 mi.append(task)
#                 mi[1] = task[1]
#                 found = True
#                 break
#
#         if not found:
#             noMachine += 1
#             schedule.append(["Machine" + str(noMachine), task[1], task])
#
#     return schedule
#
# jobs = [(7, 8, 't1'), (3, 7, 't2'), (1, 5, 't3'), (5, 9, 't4'), (0, 2, 't5'), (6, 8, 't6'), (1, 6, 't7')]
# schedule = jobScheduling(jobs)
# print(len(schedule))
# print(schedule)






def jobScheduling(jobs):
    L = sorted(jobs)
    schedule = []
    noMachine = 0

    while L:
        task = L.pop(0)
        found = False
        for mi in schedule:
            if mi[1] <= task[0]:
                mi.append(task)
                mi[1] = task[1]
                found = True
                break
        if not found:
            noMachine += 1
            schedule.append(["Machine"+str(noMachine), task[1], task])

    return schedule


jobs = [(7, 8, 't1'), (3, 7, 't2'), (1, 5, 't3'), (5, 9, 't4'), (0, 2, 't5'), (6, 8, 't6'), (1, 6, 't7')]
schedule = jobScheduling(jobs)
print(len(schedule))
print(schedule)






















