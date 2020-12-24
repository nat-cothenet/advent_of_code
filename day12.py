import copy
import math


class Position:
    def __init__(self, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.direction = direction

    def turn(self, direction, degrees):
        if direction == "R":
            self.direction -= degrees
        elif direction == "L":
            self.direction += degrees
        else:
            raise Exception("Invalid direction to turn")

    def move_forward(self, distance):
        self.x += round(distance * math.cos(math.radians(self.direction)), 6)
        self.y += round(distance * math.sin(math.radians(self.direction)), 6)

    def move_cardinal(self, direction, distance):
        if direction == "N":
            self.y += distance
        elif direction == "S":
            self.y -= distance
        elif direction == "E":
            self.x += distance
        elif direction == "W":
            self.x -= distance
        else:
            raise Exception("Invalid cardinal direction")

    def move(self, instruction):
        if len(instruction) <= 1:
            return None
        direction = instruction[:1]
        amount = int(instruction[1:])
        if direction == "F":
            self.move_forward(amount)
        elif direction in ["L", "R"]:
            self.turn(direction, amount)
        elif direction in ["N", "S", "E", "W"]:
            self.move_cardinal(direction, amount)
        else:
            raise Exception("Invalid instruction")

    def move_forward_2(self, waypoint, amount):
        self.x += amount * waypoint.x
        self.y += amount * waypoint.y


class Waypoint:
    def __init__(self, x, y, position):
        self.x = x
        self.y = y
        self.position = position

    def turn(self, direction, degrees):
        dist = math.sqrt(self.x ** 2 + self.y ** 2)
        new_angle = math.atan2(self.y, self.x)

        if direction == "R":
            new_angle -= math.radians(degrees)
        elif direction == "L":
            new_angle += math.radians(degrees)
        else:
            raise Exception("Invalid direction to turn")

        self.x = round(dist * math.cos(new_angle), 6)
        self.y = round(dist * math.sin(new_angle), 6)

    def move_cardinal(self, direction, distance):
        if direction == "N":
            self.y += distance
        elif direction == "S":
            self.y -= distance
        elif direction == "E":
            self.x += distance
        elif direction == "W":
            self.x -= distance
        else:
            raise Exception("Invalid cardinal direction")

    def move(self, instruction):
        if len(instruction) <= 1:
            return None
        direction = instruction[:1]
        amount = int(instruction[1:])
        if direction in ["L", "R"]:
            self.turn(direction, amount)
        elif direction in ["N", "S", "E", "W"]:
            self.move_cardinal(direction, amount)
        else:
            raise Exception("Invalid instruction")


def get_manhattan_dist(directions, relative="position"):
    p = Position(x=0, y=0, direction=0)
    if relative == "waypoint":
        w = Waypoint(x=10, y=1, position=p)
    for d in directions:
        if relative == "position":
            p.move(d)
        elif relative == "waypoint":
            if d.startswith("F"):
                p.move_forward_2(w, int(d[1:]))
            else:
                w.move(d)

    return abs(p.x) + abs(p.y)


filename = "input_day12.txt"

with open(filename, "r") as input:
    input_file = input.read().splitlines()
directions = [i for i in input_file]

manhattan_dist_1 = get_manhattan_dist(directions, relative="position")
manhattan_dist_2 = get_manhattan_dist(directions, relative="waypoint")

print(f"Manhattan Distance (part 1):\t{manhattan_dist_1}")
print(f"Manhattan Distance (part 2):\t{manhattan_dist_2}")
