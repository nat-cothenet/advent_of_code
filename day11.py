import copy


def get_num_occupied_neighbors(row, col, seats):
    row_bounds = [-1, 0, 1]
    col_bounds = [-1, 0, 1]
    if row == 0:
        row_bounds.remove(-1)
    if row == len(seats) - 1:
        row_bounds.remove(1)
    if col == 0:
        col_bounds.remove(-1)
    if col == len(seats[0]) - 1:
        col_bounds.remove(1)
    occ = sum([seats[row + i][col + j] ==
               "#" for i in row_bounds for j in col_bounds if not (i == 0 and j == 0)])

    return occ


def get_num_occupied_neighbors_picky(row, col, seats):
    rows_ahead = [i - row for i in range(row + 1, len(seats))]
    rows_behind = [i - row for i in range(row - 1, -1, -1)]
    cols_ahead = [i - col for i in range(col + 1, len(seats[0]))]
    cols_behind = [i - col for i in range(col - 1, -1, -1)]

    coords_to_check = []
    # Directly above
    coords_to_check.append([[row + r, col] for r in rows_ahead])
    # Directly below
    coords_to_check.append([[row + r, col] for r in rows_behind])
    # Directly to the right
    coords_to_check.append([[row, col + c] for c in cols_ahead])
    # Directly to the left
    coords_to_check.append([[row, col + c] for c in cols_behind])
    # Diagonal down to the right
    coords_to_check.append(
        [[row + i, col + i] for i in rows_ahead if i in cols_ahead])
    # Diagonal down to the left
    coords_to_check.append(
        [[row + i, col - i] for i in rows_ahead if - i in cols_behind])
    # Diagonal up to the right
    coords_to_check.append(
        [[row + i, col - i] for i in rows_behind if - i in cols_ahead])
    # Diagonal up to the left
    coords_to_check.append(
        [[row + i, col + i] for i in rows_behind if i in cols_behind])

    occ = 0
    for coord_list in coords_to_check:
        for coord in coord_list:
            val = seats[coord[0]][coord[1]]
            if val == "L":
                break
            if val == "#":
                occ += 1
                break

    return occ


def seat_round(seats, picky=False, num_occ_allowed=4):
    new_seating = copy.deepcopy(seats)
    for row in range(len(seats)):
        new_seating[row] = list(new_seating[row])
        for col in range(len(seats[row])):
            if picky:
                num_occupied = get_num_occupied_neighbors_picky(
                    row, col, seats)
            else:
                num_occupied = get_num_occupied_neighbors(row, col, seats)
            if seats[row][col] == "L" and num_occupied == 0:
                new_seating[row][col] = "#"
            elif seats[row][col] == "#" and num_occupied >= num_occ_allowed:
                new_seating[row][col] = "L"
        new_seating[row] = "".join(new_seating[row])
    return new_seating


def seat_until_stable(seats, picky=False, num_occ_allowed=4):
    new_seats = None
    timeout_num_intervals = 999

    for i in range(timeout_num_intervals):
        new_seats = seat_round(seats=seats, picky=picky,
                               num_occ_allowed=num_occ_allowed)
        if new_seats == seats:
            return seats
        else:
            seats = new_seats
    return "Does not stabilize"


def count_occupied_total(seats, occupied_str="#"):
    occ = 0
    for row in seats:
        occ += row.count(occupied_str)
    return occ


filename = "input_day11.txt"

with open(filename, "r") as input:
    input_file = input.read().splitlines()
seating = [i for i in input_file]

stable_seating = seat_until_stable(seating)
num_occupied = count_occupied_total(stable_seating)
stable_seating_picky = seat_until_stable(
    seating, picky=True, num_occ_allowed=5)
num_occupied_picky = count_occupied_total(stable_seating_picky)


print(f"Num occupied seats when stable:\t{num_occupied}")
print(f"Num occupied seats when stable (picky):\t{num_occupied_picky}")
