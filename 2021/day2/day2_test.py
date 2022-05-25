import day2


def test_get_position():
    input_txt = ["forward 5",
                 "down 5",
                 "forward 8",
                 "up 3",
                 "down 8",
                 "forward 2"]
    position = day2.get_position(input_txt)
    assert position == (15, 10), f"Combinations should be (15, 10), but is {position}"


def test_get_submarine_position():
    input_txt = ["forward 5",
                 "down 5",
                 "forward 8",
                 "up 3",
                 "down 8",
                 "forward 2"]
    s = day2.Submarine()
    position = s.get_position(input_txt)
    assert position == (15, 60), f"Combinations should be (15, 60), but is {position}"