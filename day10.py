import copy
from pprint import pprint


def find_all_diffs(adapter_list):
    adapter_list_high = copy.deepcopy(adapter_list)
    adapter_list_high.append(max(adapter_list)+3)
    adapter_list_high.sort()

    adapter_list_low = copy.deepcopy(adapter_list)
    adapter_list_low.insert(0, 0)
    adapter_list_low.sort()

    list_diffs = [h - l for h, l in zip(adapter_list_high, adapter_list_low)]
    return list_diffs


def find_num_in_diffs(diff_list, num):
    return diff_list.count(num)


def calc_num_combinations(adapter_list):
    my_adapter_list = copy.deepcopy(adapter_list)
    my_adapter_list.append(max(my_adapter_list) + 3)
    my_adapter_list.sort()
    combos, _ = get_all_combinations_num(
        my_adapter_list, curr_adapter=0, cache={})
    return combos


def get_all_combinations(adapter_list, curr_adapter=0, cache={}):
    if curr_adapter == max(adapter_list):
        print("Reached the end!")
        cache[curr_adapter] = [[curr_adapter]]
        return [[curr_adapter]], cache

    options = []
    for n in next_valid(adapter_list, curr_adapter):
        new_options = cache.get(n)
        if new_options:
            print(f"Using cache for {n}")
        if not new_options:
            print(f"Getting options for {n}")
            new_options, new_cache = get_all_combinations(
                adapter_list, n, cache)
            cache.update(new_cache)
        print(f"Extending options for {n} after {curr_adapter}")
        options.extend(new_options)
    print(f"Adding {curr_adapter} to my lists")
    for i in range(len(options)):
        options[i].extend([curr_adapter])
    print(f"Caching {curr_adapter}")
    cache[curr_adapter] = options
    return options, cache


def get_all_combinations_num(adapter_list, curr_adapter=0, cache={}):
    if curr_adapter == max(adapter_list):
        cache[curr_adapter] = 1
        return 1, cache

    options = 0
    for n in next_valid(adapter_list, curr_adapter):
        new_options = cache.get(n)
        if not new_options:
            new_options, new_cache = get_all_combinations_num(
                adapter_list, n, cache)
            cache.update(new_cache)
        options += new_options
    cache[curr_adapter] = options
    return options, cache

def next_valid(adapter_list, adapter=0):
    return [a for a in adapter_list
            if (a - adapter <= 3 and a - adapter > 0)]


filename = "input_day10.txt"
n_1 = 1
n_2 = 3

with open(filename, "r") as input:
    input_file = input.read().splitlines()
input_file = [int(i) for i in input_file]
print(input_file)

diff_list = find_all_diffs(input_file)
num_diffs_1 = find_num_in_diffs(diff_list, n_1)
num_diffs_2 = find_num_in_diffs(diff_list, n_2)

print(diff_list)
print(f"Num of adapters with diff {n_1}:\t{num_diffs_1}")
print(f"Num of adapters with diff {n_2}:\t{num_diffs_2}")
print(f"Product:\t{num_diffs_1 * num_diffs_2}")

num_combos = calc_num_combinations(input_file)
print(f"Num combos:\t{num_combos}")
