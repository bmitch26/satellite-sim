# cubesat/scheduler.py

import time
from rich import print

class Scheduler:
    def __init__(self, tasks, interval=1.0):
        self.tasks = tasks
        self.interval = interval

    
    # def run(self, total_ticks=10):
    #     from cubesat.command_parser import CommandParser
    #     import queue

    #     state = {"tick": 0}
    #     command_queue = queue.Queue()
    #     parser = CommandParser()

    #     for _ in range(total_ticks):
    #         # Print Tick Header
    #         print(f"\n[bold cyan]TICK {state['tick']} ─────────────────────────────────────[/bold cyan]")

    #         # Run scheduled tasks
    #         for task in self.tasks:
    #             if task.should_run(state["tick"]):
    #                 task.run(state)

    #         # CLI Input for this tick (no threading required anymore!)
    #         cmd_str = input("Ground Station CLI - Type JSON command or just press Enter:").strip()
    #         if cmd_str:
    #             try:
    #                 cmd = parser.parse(cmd_str)
    #                 command_queue.put(cmd)
    #             except ValueError as e:
    #                 print(f"CLI Error: {e}")

    #         # Pass the shared queue back to the CommandHandler
    #         state["command_queue"] = command_queue

    #         state["tick"] += 1

    def run(self, total_ticks=10, manual=False):
        from cubesat.command_parser import CommandParser
        import queue
        import time

        state = {"tick": 0}
        command_queue = queue.Queue()
        parser = CommandParser()

        for _ in range(total_ticks):
            print(f"\n[bold cyan]TICK {state['tick']} ─────────────────────────────────────[/bold cyan]")

            # Ask for CLI command BEFORE running tasks
            cmd_str = input("Ground Station CLI - Type JSON command or press Enter: ").strip()
            if cmd_str:
                try:
                    cmd = parser.parse(cmd_str)
                    command_queue.put(cmd)
                except ValueError as e:
                    print(f"[red]CLI Error: {e}[/red]")

            # Make the queue available to all tasks
            state["command_queue"] = command_queue

            # Run scheduled tasks
            for task in self.tasks:
                if task.should_run(state["tick"]):
                    task.run(state)

            # Pause
            if manual:
                input("Press Enter to continue to the next tick.")
            else:
                time.sleep(self.interval)

            state["tick"] += 1
