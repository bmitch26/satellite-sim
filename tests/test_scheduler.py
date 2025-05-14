# tests/test_scheduler.py

from cubesat.scheduler import Scheduler
from cubesat.command_handler import CommandHandlerTask
from cubesat.utils import BaseTask
from unittest.mock import patch
import queue

class DummyTask(BaseTask):
    def run(self, state):
        self.last_run_tick = state["tick"]
        print("DummyTask ran.")

def test_scheduler_runs_task(capfd):
    q = queue.Queue()
    tasks = [CommandHandlerTask("CommandHandler", interval=1), DummyTask("Dummy")]
    scheduler = Scheduler(tasks, interval=0.1)

    with patch("builtins.input", return_value=""):
        scheduler.run(total_ticks=1)

    out, _ = capfd.readouterr()
    assert "DummyTask ran." in out
