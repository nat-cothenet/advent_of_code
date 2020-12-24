import day12


def test_instructions_stage1():
    input_dirs = ["F10",
                  "N3",
                  "F7",
                  "R90",
                  "F11"
                  ]
    out = day12.get_manhattan_dist(input_dirs, relative="position")
    assert out == 25, f"Incorrect Manhattan distance calc; result was {out}"


def test_instructions_stage2():
    input_dirs = ["F10",
                  "N3",
                  "F7",
                  "R90",
                  "F11"
                  ]
    out = day12.get_manhattan_dist(input_dirs, relative="waypoint")
    assert out == 286, f"Incorrect Manhattan distance calc; result was {out}"
