//// SystemState.hpp ////

#pragma once

#include <mutex>


class SystemState {
public:
    float oxygenLevel = 100.0f; // starts fully oxygenated
    float batteryLevel = 100.0f; // starts with full battery
    bool faultRaised = false; // for fault logic

    std::mutex mutex;  // protects shared access to the above
};