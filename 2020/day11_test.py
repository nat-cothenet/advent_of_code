import day11


def test_seating_round_1():
    input_seats = ["L.LL.LL.LL",
                   "LLLLLLL.LL",
                   "L.L.L..L..",
                   "LLLL.LL.LL",
                   "L.LL.LL.LL",
                   "L.LLLLL.LL",
                   "..L.L.....",
                   "LLLLLLLLLL",
                   "L.LLLLLL.L",
                   "L.LLLLL.LL"
                   ]
    output = [
        "#.##.##.##",
        "#######.##",
        "#.#.#..#..",
        "####.##.##",
        "#.##.##.##",
        "#.#####.##",
        "..#.#.....",
        "##########",
        "#.######.#",
        "#.#####.##"
    ]
    assert day11.seat_round(
        input_seats) == output, "Round 1 seating is incorrect"


def test_picky_seating_round_2():
    input_seats = ["L.LL.LL.LL",
                   "LLLLLLL.LL",
                   "L.L.L..L..",
                   "LLLL.LL.LL",
                   "L.LL.LL.LL",
                   "L.LLLLL.LL",
                   "..L.L.....",
                   "LLLLLLLLLL",
                   "L.LLLLLL.L",
                   "L.LLLLL.LL"
                   ]
    output = [
        "#.LL.LL.L#",
        "#LLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLL#",
        "#.LLLLLL.L",
        "#.LLLLL.L#",
    ]

    two_rounds = day11.seat_round(input_seats, picky=True, num_occ_allowed=5)
    two_rounds = day11.seat_round(two_rounds, picky=True, num_occ_allowed=5)
    assert two_rounds == output, "Round 2 picky seating is incorrect"


def test_seating_stabilize():
    input_seats = ["L.LL.LL.LL",
                   "LLLLLLL.LL",
                   "L.L.L..L..",
                   "LLLL.LL.LL",
                   "L.LL.LL.LL",
                   "L.LLLLL.LL",
                   "..L.L.....",
                   "LLLLLLLLLL",
                   "L.LLLLLL.L",
                   "L.LLLLL.LL"
                   ]
    output = [
        "#.#L.L#.##",
        "#LLL#LL.L#",
        "L.#.L..#..",
        "#L##.##.L#",
        "#.#L.LL.LL",
        "#.#L#L#.##",
        "..L.L.....",
        "#L#L##L#L#",
        "#.LLLLLL.L",
        "#.#L#L#.##"
    ]
    assert day11.seat_until_stable(
        input_seats, picky=False, num_occ_allowed=4) == output, "Stabilized seating is incorrect"


def test_seating_stabilize_picky():
    input_seats = ["L.LL.LL.LL",
                   "LLLLLLL.LL",
                   "L.L.L..L..",
                   "LLLL.LL.LL",
                   "L.LL.LL.LL",
                   "L.LLLLL.LL",
                   "..L.L.....",
                   "LLLLLLLLLL",
                   "L.LLLLLL.L",
                   "L.LLLLL.LL"
                   ]
    output = [
        "#.L#.L#.L#",
        "#LLLLLL.LL",
        "L.L.L..#..",
        "##L#.#L.L#",
        "L.L#.LL.L#",
        "#.LLLL#.LL",
        "..#.L.....",
        "LLL###LLL#",
        "#.LLLLL#.L",
        "#.L#LL#.L#"
    ]
    assert day11.seat_until_stable(
        input_seats, picky=True, num_occ_allowed=5) == output, "Picky stabilized seating is incorrect"


def test_occupied_calc():
    seating = [
        "#.#L.L#.##",
        "#LLL#LL.L#",
        "L.#.L..#..",
        "#L##.##.L#",
        "#.#L.LL.LL",
        "#.#L#L#.##",
        "..L.L.....",
        "#L#L##L#L#",
        "#.LLLLLL.L",
        "#.#L#L#.##"
    ]
    assert day11.count_occupied_total(
        seating) == 37, "Num occupied should be 37"


def test_occupied_seat():
    seating = [
        "#.#L.L#.##",
        "#LLL#LL.L#",
        "L.#.L..#..",
        "#L##.##.L#",
        "#.#L.LL.LL",
        "#.#L#L#.##",
        "..L.L.....",
        "#L#L##L#L#",
        "#.LLLLLL.L",
        "#.#L#L#.##"
    ]
    assert day11.get_num_occupied_neighbors(1, 9, seating) == 2, "Should be 2"


def test_occupied_seat_picky1():
    seating = [
        ".......#.",
        "...#.....",
        ".#.......",
        ".........",
        "..#L....#",
        "....#....",
        ".........",
        "#........",
        "...#....."
    ]
    occ = day11.get_num_occupied_neighbors_picky(
        4, 3, seating)
    assert occ == 8, f"Should be 8, instead got {occ}"


def test_occupied_seat_picky2():
    seating = [
        ".............",
        ".L.L.#.#.#.#.",
        "............."
    ]
    assert day11.get_num_occupied_neighbors_picky(
        1, 1, seating) == 0, "Should be 0"

def test_occupied_seat_picky3():
    seating = [
        ".##.##.",
        "#.#.#.#",
        "##...##",
        "...L...",
        "##...##",
        "#.#.#.#",
        ".##.##."
    ]
    assert day11.get_num_occupied_neighbors_picky(
        3, 3, seating) == 0, "Should be 0"
