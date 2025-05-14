# cubesat/command_handler.py

class CommandHandlerTask:
    def __init__(self, name, command_queue=None):
        self.name = name
        self.command_queue = command_queue if command_queue is not None else []

    def run(self, state):
        if self.command_queue:
            command = self.command_queue.pop(0)
            print(f"[CommandHandlerTask] Tick {state['tick']}: Executing command: {command}")
        else:
            print(f"[CommandHandlerTask] Tick {state['tick']}: No commands to process.")
