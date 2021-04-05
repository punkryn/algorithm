def get_optimal_value(capacity, weights, values, names):
    size = len(weights)
    vpw = [(values[i] / weights[i], weights[i], names[i]) for i in range(size)]

    densities = sorted(vpw, reverse = True)

    finalValue = 0
    for i, v in enumerate(densities):
        a = min(capacity, v[1])
        finalValue += a * v[0]
        print(v[2], a, "gram is taken")
        capacity -= a
        if capacity == 0:
            break
    return finalValue

capacity = 3900
values = [4500, 5000, 5500, 60000, 65000, 70000, 750000, 800000, 850000, 900000]
weights = [50, 500, 11, 60, 100, 35, 30, 40, 5000, 90]
names = ["가", "나", "다", '라', '마', '바', '사', '아', '자', '차']
opt_value = get_optimal_value(capacity, weights, values, names)
print("value of the knapsack is", opt_value)