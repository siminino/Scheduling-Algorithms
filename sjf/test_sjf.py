from unittest import TestCase
from sjf import Sjf
from schedulingalg.process.process import Process

class JsfTestCase(TestCase):

    def setUp(self):
        self.schedule = Sjf()

    def test_sjf_objects_should_be_created(self):
        self.assertTrue(self.schedule)

    def test_add_process_on_round_robin_list(self):
        process = Process(20)
        self.schedule.add_process(process)
        self.assertTrue(process in self.schedule.list_process)

    def test_process_should_be_ordering_by_length(self):
        process_1 = Process(20)
        process_2 = Process(10)
        self.schedule.add_process(process_1)
        self.schedule.add_process(process_2)
        self.schedule.ordering_process();
        self.assertEqual(process_1, self.schedule.list_process[1])
        self.assertEqual(process_2, self.schedule.list_process[0])

    def test_process_should_be_ordering_by_length_with_4_process(self):
        process_1 = Process(20)
        process_2 = Process(10)
        process_3 = Process(40)
        process_4 = Process(30)
        self.schedule.add_process(process_1)
        self.schedule.add_process(process_2)
        self.schedule.add_process(process_3)
        self.schedule.add_process(process_4)
        self.schedule.ordering_process();
        self.assertEqual(process_1, self.schedule.list_process[1])
        self.assertEqual(process_2, self.schedule.list_process[0])
        self.assertEqual(process_3, self.schedule.list_process[3])
        self.assertEqual(process_4, self.schedule.list_process[2])

    def test_all_process_should_be_runed(self):
        process_1 = Process(20)
        process_2 = Process(10)
        process_3 = Process(40)
        process_4 = Process(30)
        self.schedule.list_process = [process_1, process_2, process_3, process_4]
        self.schedule.run()
        self.assertFalse(self.schedule.list_process)
