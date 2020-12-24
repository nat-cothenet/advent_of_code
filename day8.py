import copy


def parse_lines(input_text):
    action = input_text.split(" ")[0]
    amount = int(input_text.split(" ")[1])
    return [action, amount, 0]


def run_game(input_file):
    acc = 0
    index = 0
    curr = input_file[index]
    curr[2] += 1
    while curr[2] <= 1 and index < len(input_file):
        action = curr[0]
        num = curr[1]
        if action == "nop":
            index += 1
        elif action == "acc":
            acc += num
            index += 1
        elif action == "jmp":
            index += num
        else:
            raise Exception("Invalid command")
        if index >= len(input_file):
            break
        curr = input_file[index]
        curr[2] += 1
    status = "success" if index >= len(input_file) else "failed"
    for idx, val in enumerate(input_file):
        val[2] = 0
        input_file[idx] = val
    return acc, status


def flip_command(input_file):
    for idx, val in enumerate(input_file):
        if val[0] not in ["jmp", "nop"]:
            continue
        revised = copy.deepcopy(input_file)
        if val[0] == "jmp":
            revised[idx][0] = "nop"
        elif val[0] == "nop":
            revised[idx][0] = "jmp"
        check = run_game(revised)
        if check[1] == "success":
            return check[0]
    return -999


filename = "input_day8.txt"

with open(filename, "r") as input:
    input_file = input.read().splitlines()
input_file = [parse_lines(i) for i in input_file]
check_acc = run_game(input_file)[0]
print(f"Acc:\t{check_acc}")
flip_acc = flip_command(input_file)
print(f"Flipped acc:\t{flip_acc}")
