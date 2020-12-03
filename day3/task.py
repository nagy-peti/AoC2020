from functools import reduce
data = []


def get_input():
    with open('in.txt') as f:
        for string_line in f:
            data.append(string_line.replace('\n', ''))


def task(right=3, down=1):
    x = 0
    y = 0
    c = 0
    while y < len(data)-1:
        # print(y,x)
        x = x+right
        y = y+down
        if x >= len(data[y]):
            x = x-len(data[y])
        if data[y][x] == "#":
            c += 1
            # print("ADDED C",c)
        # print(data[y])
    return c


get_input()
print("trees:", task())

movements = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2}]
nums = []

for m in movements:
    num = task(right=m["right"], down=m["down"])
    print("trees:", num)
    nums.append(num)

print("multipl", reduce(lambda x, y: x*y, nums))
