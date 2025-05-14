# cubesat/utils.py

class BaseTask:
    def __init__(self, name, interval=1):
        self.name = name
        self.interval = interval
        self.last_run_tick = -1

    def should_run(self, current_tick):
        return (current_tick - self.last_run_tick) >= self.interval

    def run(self, state):
        raise NotImplementedError
