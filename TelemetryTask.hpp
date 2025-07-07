//// TelemetryTask.hpp ////

/*
This will simulate updating system telemetry values at fixed intervals.
*/

#pragma once

#include "Task.hpp"
#include "SystemState.hpp"
#include <chrono>
#include <thread>
#include <mutex>
#include <random>
#include <iostream>
#include <algorithm>

class TelemetryTask : public Task {
public:
    TelemetryTask(SystemState& sharedState, int intervalMs = 1000) 
    : Task("TelemetryTask"), state(sharedState), interval(intervalMs) {}

protected:
    void run() override {
        std::default_random_engine generator(std::random_device{}());
        std::uniform_real_distribution<float> oxygenDrift(-0.5f, 0.5f);
        std::uniform_real_distribution<float> batteryDrain(-1.0f, -0.2f);

        while (running) {
            {
            std::lock_guard<std::mutex> lock(state.mutex);
            state.oxygenLevel += oxygenDrift(generator);
            state.batteryLevel += batteryDrain(generator);

            // clamp values for realism
            state.oxygenLevel = std::max(0.0f, std::min(100.0f, state.oxygenLevel));
            state.batteryLevel = std::max(0.0f, std::min(100.0f, state.batteryLevel));

            // optionally print for debug 
            std::cout << "Telemetry Oxygen: " << state.oxygenLevel << "\n"
                      << "Battery %: " << state.batteryLevel << "%" << "\n";
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(interval));
        }
    }

private:
    SystemState& state;
    int interval;   // milliseconds between updates
};