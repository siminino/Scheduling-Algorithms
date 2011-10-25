import unittest
from process import Process

class ProcessTestCase(unittest.TestCase):

    def setUp(self):
        self.process = Process(20)

    def test_create_process_object(self):
        self.assertTrue(self.process)

    def test_process_should_have_task(self):
        self.assertEqual(self.process.task, 20)

    def test_run_process_should_work_one_task(self):
        self.process.run()
        self.assertEqual(self.process.task, 19)

    def test_run_process_with_time_should_work_tasks_to_timeout(self):
        self.process.run_time(10)
        self.assertEqual(self.process.task, 10)

    def test_run_process_with_time_greater_then_tasks_should_close_process(self):
        self.process.run_time(30)
        self.assertEqual(self.process.task, 0)

