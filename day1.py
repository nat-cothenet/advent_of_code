import pandas as pd
import numpy as np


def find_sum_to(data, sum_val):
    for idx1, i in enumerate(data[:-2]):
        val1 = i
        for idx2, j in enumerate(data[idx1 + 1:-1]):
            val2 = j
            for k in data[idx1 + idx2 + 1:]:
                val3 = k
                if val1 + val2 + val3 == sum_val:
                    return [val1, val2, val3]
    return None


input_data = pd.read_csv("input_day1.csv")
vals = find_sum_to(list(input_data['input_data'].values), 2020)
product = np.prod(vals)
print(f"Values: \t{vals}")
print(f"Product:\t{product}")