import pandas as pd
import numpy as np
import math
from pprint import pprint
import re

req_fields = [
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
]

req_fields_dict = {
    "byr": [str(i) for i in range(1920, 2002+1)],
    "iyr": [str(i) for i in range(2010, 2020+1)],
    "eyr": [str(i) for i in range(2020, 2030+1)],
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "hgt": {"cm": [str(i) for i in range(150, 193+1)],
            "in": [str(i) for i in range(59, 76+1)]},
    "hcl": "^#[a-fA-F0-9]{6}$",
    "pid": "^[0-9]{9}$"
}


def parse_data(data):
    passport_data = []
    tmp = {}
    for r in range(len(data)):
        row_data = data.iloc[r, 0]
        if isinstance(row_data, str):
            elems = row_data.split(" ")
            for e in elems:
                field = e.split(":")
                tmp[field[0]] = field[1]
            if r == len(data) - 1:
                passport_data.append(tmp)
        else:
            passport_data.append(tmp)
            tmp = {}

    return passport_data


def is_valid_1(passport_entry, fields):
    return set(fields).issubset(set(passport_entry.keys()))


def is_valid_2(passport_entry, field_dict, verbose=False):
    if not set(field_dict.keys()).issubset(set(passport_entry.keys())):
        return False
    for field, entry in passport_entry.items():
        if field in ["byr", "iyr", "eyr", "ecl"]:
            if entry not in field_dict.get(field):
                if verbose:
                    print(f"{field}\t{entry}\t{field_dict.get(field)}")
                return False
        elif field == "hgt":
            units = entry[-2:]
            if not field_dict.get(field).get(units):
                if verbose:
                    print(units)
                return False
            elif entry[:-2] not in field_dict.get(field).get(units):
                if verbose:
                    print(f"{entry[:-2] }\t{field_dict.get(field).get(units)}")
                return False
        elif field in ["hcl", "pid"]:
            if not re.findall(field_dict.get(field), entry):
                if verbose:
                    print(f"{field_dict.get(field)}\t{entry}")
                return False
    return True


passport_data_raw = pd.read_csv("input_day4.csv",
                                header=None, skip_blank_lines=False)
passport_data = parse_data(passport_data_raw)
# pprint(passport_data)

num_valid_1 = 0
num_valid_2 = 0
for passport in passport_data:
    if is_valid_1(passport, req_fields):
        num_valid_1 += 1
    if is_valid_2(passport, req_fields_dict):
        num_valid_2 += 1

print(f"Num valid, pt 1:\t{num_valid_1}")
print(f"Num valid, pt 2:\t{num_valid_2}")
