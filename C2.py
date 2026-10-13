def parallel_resistance(resistors):
    inverse_sum = 0
    for r in resistors:
        inverse_sum += 1 / r
    return 1 / inverse_sum

print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))
print("parallel_resistance([100, 200, 300]) ->", parallel_resistance([100, 200, 300]))
