from cubesat.scheduler import Scheduler
from cubesat.telemetry import TelemetryTask
from cubesat.command_handler import CommandHandlerTask
from cubesat.fault_monitor import FaultMonitorTask
from cubesat.attitude_control import AttitudeControlTask
from cubesat.command_parser import CommandParser
from cubesat.orbit import OrbitTask
from cubesat.sunlight import SunlightModelTask
from cubesat.mode_manager import ModeManagerTask

import json
import threading
import queue
import os
from rich import print

# === CLI Command Input Setup ===
# command_queue = queue.Queue()
# parser = CommandParser()

# def command_input_loop():
#     # print("[bold purple]Ground Station CLI: Type JSON commands (or 'exit'):[/bold purple]")
#     while True:
#         cmd_str = input(">>> ").strip()
#         if not cmd_str:
#             continue  # Ignore empty input (like pressing Enter)

#         if cmd_str.lower() == "exit":
#             break
#         elif cmd_str.lower() == "shutdown":
#             print("[CLI] Shutdown requested. Exiting simulation...")
#             os._exit(0)
        
#         try:
#             cmd = parser.parse(cmd_str)
#             command_queue.put(cmd)
#         except ValueError as e:
#             print(f"[CLI Error] {e}")


# # Start CLI in a background thread
# input_thread = threading.Thread(target=command_input_loop, daemon=True)
# input_thread.start()

# === Initialize shared telemetry buffer ===
telemetry_buffer = []

# === Register all tasks ===
tasks = [
    TelemetryTask("Telemetry", telemetry_buffer, interval=2),
    CommandHandlerTask("CommandHandler", interval=1),
    FaultMonitorTask("FaultMonitor", interval=3),
    AttitudeControlTask("AttitudeControl", interval=2),
    OrbitTask("Orbit", interval=1),
    SunlightModelTask("Sunlight", interval=1),
    ModeManagerTask("ModeManager", interval=1),
]

# === Create scheduler and run simulation ===
scheduler = Scheduler(tasks, interval=4.0)

# === Ask user how they want to run it ===
choice = input("Run in manual mode? (y/n): ").lower().strip()
manual_mode = choice == "y"

scheduler.run(total_ticks=20, manual=manual_mode)

# === Dump buffered telemetry to file ===
with open("telemetry_log.json", "w") as f:
    json.dump(telemetry_buffer, f, indent=2)

print("\nGround Station: Dumped telemetry to telemetry_log.json")
