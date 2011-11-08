class RoundRobin:
    def __init__(self, quantum):
        self.quantum = int(quantum)
        self.list_process = []

    def add_process(self, process):
        self.list_process.append(process)

    def run_process(self):
        for process in self.list_process:
            process.run_time(self.quantum)
            if not process.task:
                self.list_process.remove(process)

    def run(self):
        while self.list_process != []:
            self.run_process()

