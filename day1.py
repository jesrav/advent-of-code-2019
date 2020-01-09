from math import floor


def get_fuel_required(mass):
    return floor(mass / 3) - 2


with open("data/day1.txt", "r") as input:
    results = [get_fuel_required(int(line.rstrip())) for line in input]

print(sum(results))