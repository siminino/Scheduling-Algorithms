#!/usr/bin/env python
from process.process import Process

class RoundRobin:
    def __init__(self, quantum):
        self.quantum = quantum
