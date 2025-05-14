# tests/test_scheduler.py

from cubesat.scheduler import Scheduler
from cubesat.utils import BaseTask

class DummyTask(BaseTask):
    def __init__(self):
        super().__init__("Dummy", interval=1)
        self.ran = False

    def run(self, state):
        self.ran = True
        self.last_run_tick = state["tick"]

def test_scheduler_runs_task():
    task = DummyTask()
    scheduler = Scheduler([task], interval=0.0)
    scheduler.run(total_ticks=1)
    assert task.ran
