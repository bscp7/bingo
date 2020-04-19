import random


def get_random_int(limit):
    if limit <0 and limit > 999:
        raise ValueError("Only positive numbers between 0 to 999 inclusive are allowed")
    return random.randint(1, limit)

def get_numbers(limit):
    l = list()
    for i in range(1, limit+1):
        l.append(i)

    random.shuffle(l)
    return l

def roll(limit):
    for i in get_numbers(limit):
        yield  i
