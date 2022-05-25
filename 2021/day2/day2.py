import os
import pandas as pd
os.chdir("C:/Users/natal/PycharmProjects/pythonProject/advent_of_code/2021/day2")

class Submarine:
    def __init__(self):
        self.h_pos = 0
        self.v_pos = 0
        self.aim = 0

    def down(self, amount):
        self.aim += amount

    def up(self, amount):
        self.aim -= amount

    def forward(self, amount):
        self.h_pos += amount
        self.v_pos += self.aim * amount

    def get_position(self, command_list):
        for i in command_list:
            dir, amount = i.split(" ")
            eval(f"self.{dir}({amount})")
        return self.h_pos, self.v_pos


def get_position(command_list):
    df = pd.DataFrame({"commands": command_list})
    df["direction"] = df["commands"].apply(lambda x: x.split(" ")[0])
    df["amount"] = df["commands"].apply(lambda x: int(x.split(" ")[1]))
    df.drop(columns="commands", inplace=True)
    vpos = sum(df.loc[df["direction"] == "down", "amount"]) - sum(df.loc[df["direction"] == "up", "amount"])
    hpos = sum(df.loc[df["direction"] == "forward", "amount"])
    return (hpos, vpos)


filename = "input_day2.txt"
with open(filename, "r") as input:
    input_file = input.read().splitlines()
input_file = [i for i in input_file]

position = get_position(input_file)
print(f"Position:\t{position}\t{position[0] * position[1]}")

s = Submarine()
position = s.get_position(input_file)
print(f"Position:\t{position}\t{position[0] * position[1]}")
