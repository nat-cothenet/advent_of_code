from copy import deepcopy

def play_turn(turns):
    last = turns[0]
    if last in turns[1:]:
        return turns[1:].index(last) + 1
    else:
        return 0


def play_game(starting_seq, num_turns):
    if num_turns == 0:
        return starting_seq

    turns = deepcopy(starting_seq)
    turns.reverse()
    for n in range(num_turns - len(starting_seq)):
        turns.insert(0, play_turn(turns))

    return turns[0]

input_day15 = [0, 14, 6, 20, 1, 4]
print(f"Last move:\t{play_game(input_day15, 2020)}")
print(f"Last move:\t{play_game(input_day15, 30000000)}")
