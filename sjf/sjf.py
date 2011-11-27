
class Sjf:
    def __init__(self):
        self.list_process = []

    def add_process(self, process):
        self.list_process.append(process)

    def run(self):
        self.ordering_process()
        for process in self.list_process:
            process.run_all_process()
            print 'Process #%d: OK!' % (self.list_process.index(process) + 1)

        self.list_process = []

    def ordering_process(self):
        new_list = []
        for process in self.list_process[::-1]:
            if not len(new_list):
                new_list.append(process)
                continue

            if process.task > new_list[-1].task:
                new_list.append(process)
                continue

            for new_process in new_list:
                if process.task < new_process.task:
                    new_list.insert(new_list.index(new_process), process)
                    break

        self.list_process = new_list
