import pandas as pd
from pprint import pprint


def get_elem(instr, row_list, front, back):
    if len(row_list) == 1:
        return row_list[0]
    curr_instr = instr.pop(0)
    if curr_instr == front:
        curr_row_list = row_list[:int(len(row_list) / 2)]
    elif curr_instr == back:
        curr_row_list = row_list[int(len(row_list) / 2):]
    else:
        raise Exception("Invalid instruction")
    return get_elem(instr, curr_row_list, front, back)


def get_id(x):
    row = x["row"]
    col = x["col"]
    return 8 * row + col

def get_missing_seat(seat_data):
    seat_data.sort()
    start, end = seat_data[0], seat_data[-1]
    return sorted(set(range(start, end + 1)).difference(seat_data))

bp_data = pd.read_csv("input_day5.csv",
                      header=None, skip_blank_lines=False)


# pprint(passport_data)
bp_data["row"] = bp_data.iloc[:, 0].apply(
    lambda x: get_elem(list(x[:7]), list(range(128)), "F", "B"))
bp_data["col"] = bp_data.iloc[:, 0].apply(
    lambda x: get_elem(list(x[-3:]), list(range(8)), "L", "R"))
bp_data["id"] = bp_data.apply(lambda x: get_id(x), axis=1)
pprint(bp_data.head())
print(f"Max ID:\t\t\t{max(bp_data['id'])}")
missing_seats = get_missing_seat(list(bp_data["id"].values))
print(f"Missing seat(s):\t{missing_seats}")
