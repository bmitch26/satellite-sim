# cubesat/scheduler.py

import time

class Scheduler:
    def __init__(self, tasks, interval=1.0):
        self.tasks = tasks
        self.interval = interval

    def run(self, total_ticks=10):
        state = {"tick": 0}
        for _ in range(total_ticks):
            print(f"\n[Tick {state['tick']}]")
            for task in self.tasks:
                task.run(state)
            state["tick"] += 1
            time.sleep(self.interval)