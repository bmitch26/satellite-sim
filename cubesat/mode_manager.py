## generate new task stubs

# cubesat/mode_manager.py

from cubesat.utils import BaseTask
from rich import print

class ModeManagerTask(BaseTask):
    def __init__(self, name, interval=1):
        super().__init__(name, interval)

    def run(self, state):
        self.last_run_tick = state["tick"]
        fault = state.get("fault", False)

        if fault and state.get("mode") != "SAFE":
            print(f"[green]Switching to SAFE mode due to fault.[/green]")
            state["mode"] = "SAFE"
        elif not fault and state.get("mode") == "SAFE":
            print(f"[green]Returning to NOMINAL mode.[/green]")
            state["mode"] = "NOMINAL"
        else:
            print(f"[green]Current mode: {state.get('mode', 'NOMINAL')}[/green]")
