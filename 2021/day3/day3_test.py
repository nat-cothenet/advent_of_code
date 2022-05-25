import day3


def test_get_gamma_epsilon():
    input_txt = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    report = day3.Report(input_txt)
    gamma = report.get_gamma()
    epsilon = report.get_epsilon()
    assert (gamma, epsilon) == (22, 9), f"Combinations should be (22, 9), but is {(gamma, epsilon)}"
