from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def get_bus_num(schedule, earliest_time):
    wait_times = {
        (int(bus) - int(earliest_time) % int(bus)): int(bus)
        for bus in schedule
        if str(bus).isnumeric()
    }

    min_wait_time = min(list(wait_times.keys()))
    bus = wait_times.get(min_wait_time)
    return bus, min_wait_time


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def find_sequential_bus_schedule(schedule):
    n = []
    a = []
    for idx, bus in enumerate(schedule):
        if not str(bus).isnumeric():
            continue
        n.append(int(bus))
        a.append(int(bus) - idx)

    return chinese_remainder(n, a)


filename = "input_day13.txt"

with open(filename, "r") as input:
    input_file = input.read().splitlines()

earliest_time = input_file[0]
schedule = input_file[1].split(",")

bus_num, time_waiting = get_bus_num(schedule, earliest_time)
print(
    f"Bus num: {bus_num}\tTime waiting: {time_waiting}\tProduct: {bus_num* time_waiting}")

winner = find_sequential_bus_schedule(schedule)
print(f"Winner departs at t={winner}")
