# CubeSat Flight Software (FSW) Simulator

![image](https://github.com/user-attachments/assets/65c65772-1c62-4c92-aa69-53bcdb58d39f)

## Project Summary
This project presents a modular, real-time simulation of CubeSat flight software with autonomous fault handling, telemetry logging, and ground CLI control. This project simulates a simplified real-time flight software stack for a CubeSat. It includes a round-robin scheduler, telemetry packetization, orbit and sunlight modeling, and manual override via a ground station CLI.

## Key Features
- Manual and timed tick modes for simulating time-based control
- Real-time telemetry with JSON logging (battery, temp, orbit, etc.)
- Fault injection and autonmatic SAFE mode switching
- Mode manager logic for autonomy and recovery
- Command parsing from CLI (REBOOT, SET_MODE, etc.)
- Telemetry saved to 'telemetry_log.json' for post-mission analysis
- Unit-tested CLI parser and logic with 'pytest'

## Project structure
<pre> 
├── main.py
├── cubesat/
│   ├── scheduler.py
│   ├── telemetry.py
│   ├── command_handler.py
│   ├── fault_monitor.py
│   ├── attitude_control.py
│   ├── command_parser.py
│   ├── mode_manager.py
│   ├── orbit.py
│   ├── sunlight.py
│   ├── utils.py
└── tests/
    ├── test_command_parser.py
    ├── test_fault_monitor.py
    ├── test_telemetry.py
    ├── test_scheduler.py 
</pre>

## How to run
1. Clone the repo:
git clone https://github.com/bmitch26/cubesat-fsw-sim.git
2. Install dependencies:
pip install -r requirements.txt
3. Run the simulator:
python main.py

## Sample ground station commands
{"op": "REBOOT", "target": "fault_monitor"}
{"op": "DUMP_DATA", "target": "telemetry"}
{"op": "SET_MODE", "value": "SAFE"}

## Sample Output
{
  "packet_type": "TELEMETRY",
  "packet_id": "TM-0017",
  "destination": "GROUND",
  "timestamp": "2025-05-15T13:29:55.708060",
  "tick": 17,
  "battery": 76.64,
  "temp": 32.4,
  "status": "WARN"
}

## Testing
In the terminal, run: pytest tests/
