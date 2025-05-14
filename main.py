from cubesat.scheduler import Scheduler
from cubesat.telemetry import TelemetryTask
from cubesat.command_handler import CommandHandlerTask
from cubesat.fault_monitor import FaultMonitorTask

command_queue = [
    {"op": "REBOOT", "target": "fault_monitor"},
    {"op": "DUMP_DATA", "target": "telemetry"}
]

tasks = [
    TelemetryTask("Telemetry"),
    CommandHandlerTask("CommandHandler", command_queue),
    FaultMonitorTask("FaultMonitor")
]

scheduler = Scheduler(tasks, interval=0.2)
scheduler.run(total_ticks=10)
