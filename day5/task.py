from math import floor


def get_input():
    file = open("in.txt", "r")
    lines = file.readlines()
    file.close()
    lines = list(map(lambda l: l.replace("\n", ""), lines))
    return lines


def get_row_num(seat):
    min_row_number = 0
    max_row_number = 127
    for char in seat[:-3]:
        i = floor((min_row_number+max_row_number)/2)
        if char == "F":
            max_row_number = i
        if char == "B":
            min_row_number = i+1
    return min_row_number


def get_col_num(seat):
    min_col_number = 0
    max_col_number = 7

    for char in seat[-3:]:
        i = floor((min_col_number+max_col_number)/2)
        if char == "L":
            max_col_number = i
        if char == "R":
            min_col_number = i+1
    return min_col_number


def task2(occupied_seat_ids):
    for i in range(len(occupied_seat_ids)-1):
        if occupied_seat_ids[i]+1 != occupied_seat_ids[i+1]:
            return (occupied_seat_ids[i]+1)


seats = get_input()
occupied_seat_ids = []
for seat in seats:
    row_num = get_row_num(seat)
    col_num = get_col_num(seat)
    occupied_seat_ids.append(row_num*8+col_num)

occupied_seat_ids.sort()
print("task1:", occupied_seat_ids[-1])
print("task2:", task2(occupied_seat_ids))
