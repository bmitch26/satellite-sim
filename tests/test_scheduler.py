# tests/test_scheduler.py

from cubesat.scheduler import Scheduler

class DummyTask:
    def __init__(self):
        self.ran = False

    def run(self, state):
        self.ran = True

def test_scheduler_runs_task():
    task = DummyTask()
    scheduler = Scheduler([task], interval=0.0)
    scheduler.run(total_ticks=1)
    assert task.ran
