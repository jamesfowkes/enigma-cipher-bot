import pickle
import datetime
import sys
import os

import logging
import unittest

from collections import namedtuple
from enigma.machine import EnigmaMachine

from keysheet import get_random_keysheet, get_random_initial_positions

def get_module_logger():
    return logging.getLogger(__name__)

def random():
    keysheet = get_random_keysheet()
    initial_positions = get_random_initial_positions(keysheet.machine)

    get_module_logger().info("New machine: %s", keysheet.machine)
    get_module_logger().info("Rotors: %s", ", ".join(keysheet.rotors))
    get_module_logger().info("Reflector: %s", keysheet.reflector)
    get_module_logger().info("Ring settings: %s", ", ".join(keysheet.ring_settings))
    get_module_logger().info("Plugboard: %s", keysheet.plugboard_settings)
    get_module_logger().info("Initial positions: %s", initial_positions)

    new_machine = EnigmaMachine.from_key_sheet(
            rotors=keysheet.rotors,
            reflector=keysheet.reflector,
            ring_settings=keysheet.ring_settings,
            plugboard_settings=keysheet.plugboard_settings)
    
    new_machine.set_display(initial_positions)

    return new_machine
    
if __name__ == "__main__":
    pass
