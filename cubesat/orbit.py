# cubesat/orbit.py

from cubesat.utils import BaseTask
import math
from rich import print

class OrbitTask(BaseTask):
    def __init__(self, name, interval=1):
        super().__init__(name, interval)
        self.orbit_period = 20  # ticks for full orbit

    def run(self, state):
        self.last_run_tick = state["tick"]
        angle = 2 * math.pi * (state["tick"] % self.orbit_period) / self.orbit_period
        state["position"] = {
            "lat": round(math.sin(angle) * 30, 2),
            "lon": round(math.cos(angle) * 30, 2)
        }
        print(f"[magenta]Orbit Positioning: {state['position']}[/magenta]")
