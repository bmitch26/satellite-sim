//// main.cpp ////

#include "TelemetryTask.hpp"
#include "FaultDetectionTask.hpp"
#include "SystemState.hpp"
#include "CommandTask.hpp"
#include "TelemetryBroadcastTask.hpp"

#include <iostream>
#include <thread>
#include <chrono>

int main() {
    std::cout << "--- Embedded Flight/Ground System Simulation ---" << "\n";

    // 1. create shared system state (a shared state for all tasks)
    SystemState systemState;

    // 2. instantiate telemetry task and fault detection task
    TelemetryTask telemetry(systemState, 1000); // update every 1000ms (1 second, 1 Hz updates)
    FaultDetectionTask faultDetector(systemState, 500); // 2 Hz checks
    CommandTask command(systemState, 9000); // TCP on port 9000
    TelemetryBroadcastTask telemetryBroadcast(systemState, "127.0.0.1", 9100, 1000); // UDP

    // 3. start telemetry task thread
    telemetry.start();
    faultDetector.start();
    command.start();
    telemetryBroadcast.start();

    // 4. run simulation for 100 seconds
    constexpr int sim_duration_ms = 100 * 1000;
    std::this_thread::sleep_for(std::chrono::milliseconds(sim_duration_ms));

    // 5. stop task and wait for clean (graceful) shutdown
    telemetry.stop();
    faultDetector.stop();
    command.stop();
    telemetryBroadcast.stop();

    telemetry.join();
    faultDetector.join();
    command.join();
    telemetryBroadcast.join();

    std::cout << "--- Sim End ---" << "\n";
    return 0;
}




