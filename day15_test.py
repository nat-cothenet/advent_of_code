import day15

ITERS = 2020

def test_example1():
    intro_seq = [0, 3, 6]
    final_move = day15.play_game(intro_seq, ITERS)

    assert final_move == 436, f"Error: {final_move}"


def test_example2():
    intro_seq = [1, 3, 2]
    final_move = day15.play_game(intro_seq, ITERS)

    assert final_move == 1, f"Error: {final_move}"


def test_example3():
    intro_seq = [2, 1, 3]
    final_move = day15.play_game(intro_seq, ITERS)

    assert final_move == 10, f"Error: {final_move}"


def test_example4():
    intro_seq = [1, 2, 3]
    final_move = day15.play_game(intro_seq, ITERS)

    assert final_move == 27, f"Error: {final_move}"


def test_example5():
    intro_seq = [2, 3, 1]
    final_move = day15.play_game(intro_seq, ITERS)

    assert final_move == 78, f"Error: {final_move}"

def test_example6():
    intro_seq = [3, 2, 1]
    final_move = day15.play_game(intro_seq, ITERS)

    assert final_move == 438, f"Error: {final_move}"


def test_example7():
    intro_seq = [3, 1, 2]
    final_move = day15.play_game(intro_seq, ITERS)

    assert final_move == 1836, f"Error: {final_move}"
