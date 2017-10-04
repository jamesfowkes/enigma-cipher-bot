""" keysheet.py

Usage:
    keysheet.py [--random|--wehrmacht|--kreigsmarine|--kreigsmarine-thin]

Options:

    --wehrmacht             Allow rotors I through V
    --kreigsmarine          Allow rotors I through VIII
    --kreigsmarine-thin     Allow rotors I through VIII, Beta and Gamma and B-Thin C-Thin reflectors
"""

import docopt
import logging
import string
import random

from collections import namedtuple

def get_logger():
    return logging.getLogger(__name__)

Keysheet = namedtuple("Keysheet", ["machine", "rotors", "reflector", "ring_settings", "plugboard_settings"])

def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)

def get_random_machine():
    return random.choice(["wehrmacht", "kreigsmarine", "kreigsmarine-thin"])

def get_valid_rotors(machine_type):

    valid_rotors = None

    if machine_type == "wehrmacht":
        valid_rotors = ["I", "II", "III", "IV", "V"]

    elif machine_type == "kreigsmarine":
        valid_rotors = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

    elif machine_type == "kreigsmarine-thin":
        valid_rotors = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "Beta", "Gamma"]

    if valid_rotors is None:
        raise Exception("Machine type '{}' not recognised".format(machine_type))

    return valid_rotors

def get_random_rotors(machine_type):

    valid_rotors = get_valid_rotors(machine_type)
    random_rotors = None

    if machine_type in ["wehrmacht", "kreigsmarine"]:
        random_rotors = random_combination(valid_rotors, 3)

    elif machine_type == "kreigsmarine-thin":
        random_rotors = random_combination(valid_rotors, 4)

    return random_rotors

def get_valid_reflectors(machine_type):

    valid_reflectors = None

    if machine_type in ["wehrmacht", "kreigsmarine"]:
        valid_reflectors = ["B", "C"]

    elif machine_type == "kreigsmarine-thin":
        valid_reflectors = ["B", "C", "B-Thin", "C-Thin"]

    if valid_reflectors is None:
        raise Exception("Machine type '{}' not recognised".format(machine_type))

    return valid_reflectors

def get_random_reflector(machine_type):

    valid_reflectors = get_valid_reflectors(machine_type)
    return random.choice(valid_reflectors)

def get_random_ring_settings(machine_type):

    settings = None

    if machine_type == "wehrmacht":
        settings = " ".join([random.choice(string.ascii_uppercase) for _ in range(3)])

    elif machine_type in ["kreigsmarine", "kreigsmarine-thin"]:
        settings = " ".join([random.choice(string.ascii_uppercase) for _ in range(4)])

    if settings is None:
        raise Exception("Machine type '{}' not recognised".format(machine_type))

    return settings

def get_random_plugboard(number_of_connections = 10):

    number_of_connections = min(13, number_of_connections)

    alpha = string.ascii_uppercase
    indexes = random.sample(range(0, 25), number_of_connections*2)

    first_letter_indexes = indexes[0::2]
    last_letter_indexes = indexes[1::2]

    return " ".join([alpha[f] + alpha[l] for (f, l) in zip(first_letter_indexes, last_letter_indexes)])

def get_random_initial_positions(machine_type):

    initial_positions = ""

    if machine_type == "wehrmacht":
        initial_positions = "".join([random.choice(string.ascii_uppercase) for _ in range(3)])

    elif machine_type in ["kreigsmarine", "kreigsmarine-thin"]:
        initial_positions = "".join([random.choice(string.ascii_uppercase) for _ in range(4)])

    if initial_positions is None:
        raise Exception("Machine type '{}' not recognised".format(machine_type))

    return initial_positions


def get_random_keysheet(machine_type = None):

    machine_type = machine_type or get_random_machine()

    rotors = get_random_rotors(machine_type)
    reflector = get_random_reflector(machine_type)
    ring_settings = get_random_ring_settings(machine_type)
    plugboard_settings = get_random_plugboard()

    return Keysheet(machine_type, rotors, reflector, ring_settings, plugboard_settings)

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    opts = docopt.docopt(__doc__)

    if opts["--wehrmacht"]:
        machine = "wehrmacht"
    elif opts["--kreigsmarine"]:
        machine = "kreigsmarine"
    elif opts["--kreigsmarine-thin"]:
        machine = "kreigsmarine-thin"
    elif opts["--random"]:
        machine = None

    keysheet = get_random_keysheet(machine)

    print(keysheet)
