//// FaultDetectionTask.hpp ////

/*
This task:
    - runs periodically in its own thread
    - accesses shared SystemState
    - raises warnings or critical fault messages based on defined thresholds
    - prints to console for now (logging system can be added later)
*/

// class FaultDetectionTask : public Task {
// public:
//     FaultDetectionTask(SystemState& sharedState, int intervalMs = 500);

// protected:
//     void run() override;

// private:
//     void checkForFaults();
//     SystemState& state;
//     int interval;
// };



#pragma once

#include "Task.hpp"
#include "SystemState.hpp"
#include <iostream>
#include <chrono>
#include <thread>

class FaultDetectionTask : public Task {
public:
    FaultDetectionTask(SystemState& sharedState, int intervalMs = 500) 
        : Task("FaultDetectionTask"), state(sharedState), interval(intervalMs) {}

protected:
    void run() override {
        while (running) {
            checkForFaults();
            std::this_thread::sleep_for(std::chrono::milliseconds(interval));
        }
    }

private:
    SystemState& state;
    int interval;

    void checkForFaults() {
        std::lock_guard<std::mutex> lock(state.mutex);

        // oxygen level checks
        if (state.oxygenLevel < 15.0f) {
            std::cout << "(Fault System) CRITICAL: Oxygen level critically low: " << state.oxygenLevel << "%" << "\n";
            state.faultRaised = true;
        } else if (state.oxygenLevel < 30.0f) {
            std::cout << "(Fault System) WARNING: Oxygen level below 30%: " << state.oxygenLevel << "%" << "\n";
        }


        // battery level checks
        if (state.batteryLevel < 10.0f) {
            std::cout << "(Fault System) CRITICAL: battery level critically low: " << state.batteryLevel << "%" << "\n";
            state.faultRaised = true;
        } else if (state.batteryLevel < 25.0f) {
            std::cout << "(Fault System) WARNING: battery below 25%: " << state.batteryLevel << "%" << "\n";
        } 
    }
};