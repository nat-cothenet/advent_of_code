import day13


def test_get_min_bus_num():
    min_time = 939
    schedule = ["7", "13", "x", "x", "59", "x", "31", "19"]
    bus_num, wait_time = day13.get_bus_num(schedule, min_time)
    assert bus_num == 59, f"Incorrect bus nume, chose {bus_num}"


def test_time_wait():
    min_time = 939
    schedule = ["7", "13", "x", "x", "59", "x", "31", "19"]
    bus_num, wait_time = day13.get_bus_num(schedule, min_time)
    assert wait_time == 5, f"Incorrect wait time, calculated {wait_time}"


def test_find_sequential_bus_schedule1():
    schedule = ["7", "13", "x", "x", "59", "x", "31", "19"]
    t = day13.find_sequential_bus_schedule(schedule)
    assert t == 1068781, f"Found wrong t = {t}"


def test_find_sequential_bus_schedule2():
    schedule = ["17", "x", "13", "19"]
    t = day13.find_sequential_bus_schedule(schedule)
    assert t == 3417, f"Found wrong t = {t}"


def test_find_sequential_bus_schedule3():
    schedule = ["67", "7", "59", "61"]
    t = day13.find_sequential_bus_schedule(schedule)
    assert t == 754018, f"Found wrong t = {t}"


def test_find_sequential_bus_schedule4():
    schedule = ["67", "x", "7", "59", "61"]
    t = day13.find_sequential_bus_schedule(schedule)
    assert t == 779210, f"Found wrong t = {t}"


def test_find_sequential_bus_schedule5():
    schedule = ["67", "7", "x", "59", "61"]
    t = day13.find_sequential_bus_schedule(schedule)
    assert t == 1261476, f"Found wrong t = {t}"


def test_find_sequential_bus_schedule6():
    schedule = ["1789", "37", "47", "1889"]
    t = day13.find_sequential_bus_schedule(schedule)
    assert t == 1202161486, f"Found wrong t = {t}"
