#!/usr/bin/env python

class Process:
    def __init__(self, task):
        self.task = int(task)

    def run(self):
        self.task -= 1

    def run_time(self, time):
        for ms in range(time):
            self.task -= 1
            if not self.task:
                return False
