import random
import os


def lock_key(key, user_hash):
    new_key = ''
    keys = list(user_hash)
    index = 0
    max_i = len(user_hash)
    for c in key:
        new_key += chr(ord(c) + ord(keys[index % max_i]))
        index += 1
    return new_key


def unlock_key(key, user_hash):
    new_key = ''
    keys = list(user_hash)
    index = 0
    max_i = len(user_hash)
    for c in key:
        new_key += chr(ord(c) - ord(keys[index % max_i]))
        index += 1
    return new_key


def gen_key(length):
    pss = '$'
    for a in range(1, length):
        par = random.randint(1, 6)
        if par > 5:
            pss += '_'
        elif par == 2:
            pss += str(random.randint(0, 9))
        else:
            s = chr(random.randint(65, 91)).lower()
            if random.randint(1, 3) == 1:
                pss += s
            else:
                pss += s.upper()
    return pss


def gen_code(length):
    length -= 1
    return random.randint(10 ** length, 10 ** (length + 1) - 1)


def strong_alg(string):
    with open(f'{os.path.dirname(__file__)}\\data\\translate_1', "r") as f:
        data = f.read()
        translate1 = eval(data)

    with open(f'{os.path.dirname(__file__)}\\data\\translate_2', "r") as f:
        data = f.read()
        translate2 = eval(data)

    pss = string.lower()
    new_pss = ''
    for a in pss:
        if a in translate1 and a in translate2:
            if random.randint(0, 2) == 0:
                new_pss += translate1[a]
            else:
                new_pss += translate2[a]
        else:
            new_pss += a
            if random.randint(0, 5) >= 3:
                new_pss += '_'
    if len(new_pss) < 12:
        power = 11 - len(new_pss)
        new_pss += str(random.randint(10 ** power, 10 ** (power + 1) - 1))
    return new_pss


def simple_alg(string):
    power = random.randint(3, 8)
    return string + str(random.randint(10 ** power, 10 ** (power + 1) - 1))
