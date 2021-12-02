import day1


def test_get_num_increased():
    input_txt = [199,
                 200,
                 208,
                 210,
                 200,
                 207,
                 240,
                 269,
                 260,
                 263]
    num_increased = day1.get_num_increased(input_txt)
    assert num_increased == 7, f"Combinations should be 7, but is {num_increased}"


def test_get_triplet_increased():
    input_txt = [199,
                 200,
                 208,
                 210,
                 200,
                 207,
                 240,
                 269,
                 260,
                 263]
    num_increased = day1.get_triplet_increased(input_txt)
    assert num_increased == 5, f"Combinations should be 5, but is {num_increased}"
