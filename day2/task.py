from collections import Counter

data = []


def get_input():
    with open('in.txt') as f:
        for string_line in f:
            splitted = string_line.split()
            repeats = splitted[0].split('-')
            min_repeat = repeats[0]
            max_repeat = repeats[1]
            data.append({
                "min": int(min_repeat),
                "max": int(max_repeat),
                "letter": splitted[1][0],
                "pwd": splitted[2]}
            )


def counter(dict):
    c = Counter(dict["pwd"])
    if c[dict["letter"]] <= dict['max'] and c[dict["letter"]] >= dict['min']:
        return True
    return False


get_input()
first = len(list(filter(counter, data)))
print(first)
second = len(list(filter(
    lambda dict:
        (dict["letter"] == dict["pwd"][dict["min"]-1]) !=
        (dict["letter"] == dict["pwd"][dict["max"]-1]), data)))

print(second)
