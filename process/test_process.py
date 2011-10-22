import unittest
from process import Process

class ProcessTestCase(unittest.TestCase):

    def setUp(self):
        self.process = Process(20)

    def test_create_process_object(self):
        self.assertTrue(self.process)

    def test_process_should_have_task(self):
        self.assertEqual(self.process.task, 20)

    def test_run_process_should_worl_one_task(self):
        self.process.run()
        self.assertEqual(self.process.task, 19)

unittest.main()
