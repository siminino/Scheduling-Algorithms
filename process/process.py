class Process:
    def __init__(self, task):
        self.task = task

    def run(self):
        self.task -= 1
