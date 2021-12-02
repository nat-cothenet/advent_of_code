import day10


def test_count_num_combos():
    input_txt = [16,
                 10,
                 15,
                 5,
                 1,
                 11,
                 7,
                 19,
                 6,
                 12,
                 4]
    combos = day10.calc_num_combinations(input_txt)
    assert combos == 8, f"Combinations should be 8, but is {combos}"


def test_count_num_combos_2():
    input_txt = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3
    ]
    combos = day10.calc_num_combinations(input_txt)
    assert combos == 19208, f"Combinations should be 19208, but is {combos}"
