from copy import deepcopy

def play_game(starting_seq, num_turns):
    if num_turns == 0:
        return starting_seq
    
    game_map = {}
    for idx, n in enumerate(starting_seq[:-1]):
        game_map[n] = idx
    
    last = starting_seq[-1]
    seq = deepcopy(starting_seq)

    for idx in range(len(starting_seq) - 1, num_turns):
        seq.append(last)
        next_num = idx - game_map.get(last, idx)
        game_map[last] = idx
        last = next_num
    
    return seq[-1]


input_day15 = [0, 14, 6, 20, 1, 4]
print(f"Last move, 2,020:\t{play_game(input_day15, 2020)}")
print(f"Last move, 30,000,000:\t{play_game(input_day15, 30000000)}")


