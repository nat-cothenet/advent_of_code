import os
import pandas as pd
os.chdir("C:/Users/natal/PycharmProjects/pythonProject/advent_of_code/2021/day3")

class Report:
    def __init__(self, report):
        self.report = pd.DataFrame()
        for idx, ln in enumerate(report):
            ln_list = [int(i) for i in ln]
            self.report[idx] = pd.Series(ln_list)

    def get_epsilon(self):
        binary_gamma = self.report.mode(axis=1).iloc[:, 0].tolist()
        binary_epsilon = [1 - i for i in binary_gamma]
        epsilon = self.convert_list_to_decimal(binary_epsilon)
        return epsilon

    def get_gamma(self):
        binary_gamma = self.report.mode(axis=1).iloc[:, 0].tolist()
        gamma = self.convert_list_to_decimal(binary_gamma)
        return gamma

    def get_power_consumption(self):
        return self.get_gamma() * self.get_epsilon()

    @staticmethod
    def convert_list_to_decimal(bin_list):
        dec = 0
        for bin_pow, i in enumerate(bin_list):
            dec += i * (2 ** (len(bin_list) - bin_pow - 1))
        return dec

filename = "input_day3.txt"
with open(filename, "r") as input:
    input_file = input.read().splitlines()
input_file = [i for i in input_file]

s = Report(input_file)
gamma = s.get_gamma()
epsilon = s.get_epsilon()
power = s.get_power_consumption()
print(f"Gamma:\t{gamma}")
print(f"Epsilon:\t{epsilon}")
print(f"Power Consumption:\t{power}")
