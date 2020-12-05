# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

task1_valid_passports = []


def input_process():
    file = open("in.txt", "r")
    passport = {}
    for x in file:

        if x != "\n":
            split_it = x.replace("\n", "").split(" ")
            for item in split_it:
                item_splitted = item.split(":")
                passport[item_splitted[0]] = item_splitted[1]
        else:
            if task1_validation(passport):
                task1_valid_passports.append(passport)
            passport = {}
        # print(x)


def task1_validation(pp):
    if len(pp) == 8:
        return True
    if len(pp) == 7 and "cid" not in pp:
        return True
    if len(pp) != 8:
        return False


g_to_z = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def hgt_valid(hgt):
    return any([
        hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193,
        hgt[-2:] == "in" and 59 <= int(hgt[:-2]) <= 76
    ])


def hcl_valid(hcl):
    if (hcl[0] == "#" and len(hcl[1:]) == 6):
        for i in hcl:
            if (i in g_to_z):
                return False
            return True
    else:
        return False 



def task2_validation(pp):
    return all([
        1920 <= int(pp['byr']) <= 2002,
        2010 <= int(pp['iyr']) <= 2020,
        2010 <= int(pp['eyr']) <= 2030,
        pp['ecl'] in eye_colors,
        len(pp['pid'])==9 and pp['pid'].isnumeric(),
        hgt_valid(pp['hgt']),
        hcl_valid(pp['hcl'])
    ])


input_process()

print(len(task1_valid_passports))
task2_valid_passports = list(filter(task2_validation, task1_valid_passports))
print(len(task2_valid_passports))
