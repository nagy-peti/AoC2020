
union_of_answers = 0  # first task
intersection_of_answers = 0  # second task

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open('in.txt') as file:
    group_answers_union = set()
    group_answers_intersection = set(abc)
    for line in file:
        if line != "\n":
            new_set = set(line.replace("\n", ""))
            group_answers_union = group_answers_union.union(new_set)
            group_answers_intersection.intersection_update(new_set)
        else:
            union_of_answers += len(group_answers_union)
            intersection_of_answers += len(group_answers_intersection)
            group_answers_intersection = set(abc)
            group_answers_union.clear()

print("task 1:", union_of_answers)
print("task 2:", intersection_of_answers)
