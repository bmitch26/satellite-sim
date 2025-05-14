# cubesat/sunlight.py

from cubesat.utils import BaseTask
from rich import print

class SunlightModelTask(BaseTask):
    def __init__(self, name, interval=1):
        super().__init__(name, interval)
        self.sun_cycle = 10  # ticks of light / dark

    def run(self, state):
        self.last_run_tick = state["tick"]
        in_sunlight = (state["tick"] % (self.sun_cycle * 2)) < self.sun_cycle
        state["in_sunlight"] = in_sunlight
        state["power_mode"] = "Charging" if in_sunlight else "Battery"
        sun_status = "Present" if in_sunlight else "Not Present"
        print(f"[red]Sunlight Status: Sunlight = {sun_status}, Power Mode = {state['power_mode']}[/red]")
