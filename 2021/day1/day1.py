import os
os.chdir("C:/Users/natal/PycharmProjects/pythonProject/advent_of_code/2021/day1")


def get_triplet_increased(depth_list):
    sum_list = [sum(depth_list[i:(i+3)]) for i in range(len(depth_list)-2)]
    num_increased = get_num_increased(sum_list)
    return num_increased


def get_num_increased(depth_list):
    return sum([depth_list[i] - depth_list[i-1] > 0 for i in range(1, len(depth_list))])


filename = "input_day1.txt"
with open(filename, "r") as input:
    input_file = input.read().splitlines()
input_file = [int(i) for i in input_file]

num_increased = get_num_increased(input_file)
triplet_increased = get_triplet_increased(input_file)

print(f"Num increased:\t{num_increased}")
print(f"Triplet increased:\t{triplet_increased}")
