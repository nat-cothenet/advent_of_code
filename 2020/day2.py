import pandas as pd


def brute_force_solution(pw_series):
    def parse_line(input_string):
        input_string_list = input_string.split(" ")
        password = input_string_list[2]
        char_req = input_string_list[1][:-1]

        num_chars_str = input_string_list[0]
        num_chars_str_1 = int(num_chars_str[:num_chars_str.find("-")])
        num_chars_str_2 = int(num_chars_str[num_chars_str.find("-") + 1:])

        return password, char_req, [num_chars_str_1, num_chars_str_2]

    def is_valid_1(password, char_req, num_chars):
        num_chars = range(num_chars[0], num_chars[1] + 1)
        num_occur = password.count(char_req)
        return num_occur in num_chars

    def is_valid_2(password, char_req, num_chars):
        num_valid = 0
        for i in num_chars:
            if password[i - 1] == char_req:
                num_valid += 1
        return num_valid == 1

    num_valid_1 = 0
    num_valid_2 = 0
    for s in list(pw_series.values):
        pw, cr, nc = parse_line(s)
        if is_valid_1(pw, cr, nc):
            num_valid_1 += 1
        if is_valid_2(pw, cr, nc):
            num_valid_2 += 1

    print("More brute force")
    print(f"Num valid, q1:\t{num_valid_1}")
    print(f"Num valid, q2:\t{num_valid_2}")


def pythonic_solution(pw_series):
    def is_valid_1_row(row):
        password = row["password"]
        char_req = row["char_req"]
        num_chars = list(range(row["num_start"], row["num_end"] + 1))
        num_occur = password.count(char_req)
        return num_occur in num_chars

    def is_valid_2_row(row):
        password = row["password"]
        char_req = row["char_req"]
        num_valid = 0

        if password[row["num_start"] - 1] == char_req:
            num_valid += 1
        if password[row["num_end"] - 1] == char_req:
            num_valid += 1

        return num_valid == 1

    pw_df = pw_series.to_frame()
    pw_df["password"] = pw_series.apply(
        lambda x: x.split(" ")[2])
    pw_df["char_req"] = pw_series.apply(
        lambda x: x.split(" ")[1][:-1])
    pw_df["num_start"] = pw_series.apply(
        lambda x: int(x.split(" ")[0][:x.split(" ")[0].find("-")]))
    pw_df["num_end"] = pw_series.apply(
        lambda x: int(x.split(" ")[0][x.split(" ")[0].find("-") + 1:]))

    pw_df["valid_1"] = pw_df.apply(lambda row: is_valid_1_row(row), axis=1)
    pw_df["valid_2"] = pw_df.apply(lambda row: is_valid_2_row(row), axis=1)

    print("More Pythonic")
    print(f"Num valid, q1:\t{pw_df['valid_1'].sum()}")
    print(f"Num valid, q2:\t{pw_df['valid_2'].sum()}")


pw_df = pd.read_csv("input_day2.csv")
brute_force_solution(pw_df["input_data"])
print("-"*30)
pythonic_solution(pw_df["input_data"])
