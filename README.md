CubeSat Flight Software Simulation Project:

Goal: Build a modular simulation of CubeSat flight software capable of controlling attitude, executing scheduled tasks, and responding to telemetry/command cycles with fault-aware behavior.

Provides:

-	Reliable onboard software systems
  
-	Control of satellite behavior (attitude/orbit)
  
-	Handling of commands and telemetry
  
-	Some degree of autonomy and fault-tolerance

Aim to show:

-	Systems-level proficiency
  
-	An MVP of satellite flight software that:
  
o	Maintains orientation
o	Runs periodic tasks (like comms or data collection)
o	Accepts simple ground commands
o	Handles basic faults (e.g. sensor offline)

Overall Scope:

Simulate the flight software of an autonomous CubeSat that -- 

-	Maintains attitude using a software PID controller
  
-	Follows a basic orbital path using 2D/3D PID controller
  
-	Executes scheduled tasks (e.g., point at Earth, transmits data)
  
-	Accepts uplinked commands and downlinks telemetry logs
  
-	Detects basic faults (e.g., orientation drift, power loss) and switches modes

This shows:

-	Embedded/RT thinking: simulate a real-time loop with subsystems
  
-	Autonomy + systems: Fault modes and task logic are separated cleanly
  
-	Aerospace knowledge: Orbital concepts + satellite ops vocabulary
  
-	Misc.: Testing, modular code, and command/telemetry flows

Problem Statement:

In real-world satellite missions, flight software is responsible for managing the satellite’s state, orientation, operations, and safety, often with limited compute resources and no real-time human intervention. Building robust, fault-tolerant flight systems is essential for the success of constellations like Starlink, where thousands of satellites must function autonomously in low Earth orbit (LEO).
However, few open-source of student projects capture the core behaviors of satellite software, such as attitude control, telemetry/command handling, task execution, and fault management, especially in a testable, modular, and real-time simulation environment.

Proposed solution:

The following CubeSat simulates the embedded software of a CubeSat-class satellite. It includes:

-	A real-time execution loop for controlling systems and scheduling tasks
  
-	A PID-controlled attitude control subsystem
  
-	A command/telemetry interface to simulate uplink/downlink operations
  
-	A fault-monitoring engine that triggers recovery logic
  
-	Optional orbital tracking and visualization tools

Acceptance criteria:

Real-Time Main Loop: System executes tasks at fixed intervals (e.g., 1Hz tick), logs execution cycle time, and handles basic scheduling.

Attitude Control (PID): Satellite adjusts its orientation to reach and maintain a target quaternion or angle. Logs errors and stabilizes within tolerance.

Task Execution Framework: Periodic tasks (e.g., “take image”, “downlink telemetry”) run on a schedule and log outputs.

Fault Detection System: Detects faults (e.g., orientation drift, stuck sensor) and switches to degraded or safe mode.

Command Uplink/Telemetry Downlink: Accepts JSON/text-based ground commands and logs simulated telemetry (position, status, battery, mode).

System Modularity: Subsystems are separate modules that communicate via defined interfaces (e.g., satellite.state, control.update(), telemetry.send()).

Basic Testing: Unit tests exist for at least 3 subsystems, integration test runs a 10-minute mission simulation and checks key logs.

Preliminary Technical Design:
Modules:

core/ -- Real-time loop, mission clock, subsystem manager

control/ -- Attitude control logic, PID updates, error tracking

telemetry/ -- log creation, downlink simulation, command parsing

autonomy/ -- Fault detection, task scheduling, safe-mode logic

simulation/ -- Environment model (optional: orbital tracking, sun exposure)

interface/ -- CLI command interface

tests/ -- Unit tests, integration tests, mission replay validator
