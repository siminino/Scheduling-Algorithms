import unittest
from round_robin import RoundRobin

class RoundRobinTestCase(unittest.TestCase):

    def setUp(self):
        self.schedule = RoundRobin(2)

    def test_round_robin_objects_should_be_created(self):
        self.assertTrue(self.schedule)

    def test_should_have_quantum(self):
        self.assertEqual(self.schedule.quantum, 2)

    def test_should_add_process_to_fifos_process(self):
        

unittest.main()
