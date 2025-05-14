from cubesat.scheduler import Scheduler
from cubesat.telemetry import TelemetryTask
from cubesat.command_handler import CommandHandlerTask
from cubesat.fault_monitor import FaultMonitorTask
from cubesat.command_parser import CommandParser

parser = CommandParser()
command_queue = [
    {"op": "REBOOT", "target": "fault_monitor"},
    {"op": "DUMP_DATA", "target": "telemetry"}
]
command_queue = [parser.parse(cmd) for cmd in raw_commands]

tasks = [
    TelemetryTask("Telemetry", interval=2),
    CommandHandlerTask("CommandHandler", command_queue, interval=1),
    FaultMonitorTask("FaultMonitor", interval=3)
]

scheduler = Scheduler(tasks, interval=0.2)
scheduler.run(total_ticks=10)
