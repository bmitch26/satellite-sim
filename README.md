# CubeSat Flight Software (FSW) Simulator

A modular, real-time simulation of CubeSat flight software with autonomous fault handling, telemetry logging, and ground CLI control.

## What it does

This project simulates a simplified real-time flight software stack for a CubeSat. It includes a round-robin scheduler, telemetry packetization, orbit and sunlight modeling, and manual override via a ground station CLI.

## Key Features
- Manual and timed tick modes for simulating time-based control
- Real-time telemetry with JSON logging (battery, temp, orbit, etc.)
- Fault injection and autonmatic SAFE mode switching
- Mode manager logic for autonomy and recovery
- Command parsing from CLI (REBOOT, SET_MODE, etc.)
- Telemetry saved to 'telemetry_log.json' for post-mission analysis
- Unit-tested CLI parser and logic with 'pytest'

## Project Structure
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
