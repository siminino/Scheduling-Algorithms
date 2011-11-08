import unittest
import random
from round_robin import RoundRobin
from schedulingalg.process.process import Process

class RoundRobinTestCase(unittest.TestCase):

    def setUp(self):
        self.schedule = RoundRobin(2)

    def test_round_robin_objects_should_be_created(self):
        self.assertTrue(self.schedule)

    def test_should_have_quantum(self):
        self.assertEqual(self.schedule.quantum, 2)

    def test_add_process_on_round_robin_list(self):
        process = Process(20)
        self.schedule.add_process(process)
        self.assertTrue(process in self.schedule.list_process)

    def test_run_process_should_reduce_one_task_of_process(self):
        process = Process(20)
        self.schedule.add_process(process)
        self.schedule.run_process()
        self.assertEqual(18, process.task)

    def test_on_run_all_tasks_of_process_should_remove_process_from_list(self):
        process = Process(1)
        self.schedule.add_process(process)
        self.schedule.run_process()
        self.assertTrue(process not in self.schedule.list_process)

    def test_run_all_tests_should_clean(self):
        for i in range(8):
            self.schedule.add_process(Process(random.randint(1, 20)))

        self.schedule.run()
        self.assertEqual([], self.schedule.list_process)

