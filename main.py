from cubesat.scheduler import Scheduler
from cubesat.telemetry import TelemetryTask
from cubesat.command_handler import CommandHandlerTask
from cubesat.fault_monitor import FaultMonitorTask
from cubesat.command_parser import CommandParser
import json

parser = CommandParser()
raw_commands = [
    '{"op": "REBOOT", "target": "fault_monitor"}',
    '{"op": "DUMP_DATA", "target": "telemetry"}'
]
command_queue = [parser.parse(cmd) for cmd in raw_commands]

telemetry_buffer = []

tasks = [
    TelemetryTask("Telemetry", telemetry_buffer, interval=2),
    CommandHandlerTask("CommandHandler", command_queue, interval=1),
    FaultMonitorTask("FaultMonitor", interval=3)
]

scheduler = Scheduler(tasks, interval=0.2)
scheduler.run(total_ticks=10)

# Dump buffered telemetry at the end of run
with open("telemetry_log.json", "w") as f:
    json.dump(telemetry_buffer, f, indent=2)

print("\n[Ground Station] Dumped telemetry to telemetry_log.json ✅")
