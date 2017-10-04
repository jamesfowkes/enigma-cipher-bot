import pickle
import unittest

from collections import namedtuple

import machine

MachineCache = namedtuple("MachineCache", ["machine", "date"])

def get_module_logger():
    return logging.getLogger(__name__)

class CacheManager:

    def __init__(self, name):
        self.name = name

    def save_machine_cache(cache):
        with open('machine-cache.pickle', 'wb') as handle:
                pickle.dump(cache, handle)

    def load_machine_cache(self):
        
        machine_cache = None

        try:
            with open('machine-cache.pickle', 'rb') as handle:
                machine_cache = pickle.load(handle)
        except FileNotFoundError:
            pass

        return machine_cache

    def cache_is_valid(machine_cache, expected_date):
        valid = True
        valid = valid and (machine_cache is not None)
        valid = valid and (machine_cache.date == expected_date)

        return valid

    def delete_cache(self):
        os.remove('machine-cache.pickle')

    def get_todays_machine(self):
        
        machine_cache = load_machine_cache()

        if not cache_is_valid(machine_cache, datetime.date.today()):
            get_module_logger().info("Loaded none or invalid cache, generating new machine")
            new_machine = machine.random()
            machine_cache = MachineCache(new_machine, datetime.date.today())
            save_machine_cache(machine_cache)
        else:
            get_module_logger().info("Loaded valid cache.")
        return machine_cache.machine


class MachineCacheTest(unittest.TestCase):

    def setUp(self):
        self.manager = CacheManager("test-cache.pickle")

    def test_delete_cache(self):
        with open(self.manager.name, 'a') as a:
            a.write
            self.manager.delete_cache()