//// TelemetryBroadcastTask.hpp ////

/// This implements PHASE 2

/*
Class responsibilities:
    - CommandTask: Inherits from Task (threaded)
    - TCP Server: Listens on a port (e.g. 9000) for incoming commands
    - Parser: Parses strings into actions
    - SystemState: Updates values using std::lock_guard

Phase 1: TCP Command Uplink Implementation: to reflect how ground stations send commands to spacecraft or onboard systems using guaranteed delivery
    - Typical socket call: accept(), read(), close()
    - Thread Class Name: CommandTask
    - System Interaction: Updates shared SystemState
    - Real-world analogy: Stalink Gateway Uplink Channel
Phase 2: UDP-Based Telemetry Broadcast (Downlink Simulation): simulate real-time telemetry downlink; spacecraft streaming sensor data to ground stations continuously, regardless of request.
    - Real-world relevance: satellite broadcast telemetry via UDP to GS (TelemetryBroadcastTask sends SystemState to a receiver);
                            continuous health monitoring (used for real-time monitoring UI or logger)
                            fire-and-forget: no retransmission: I use sendto() via UDP socket
                            UDP does not guarantee delivery, but has better latency as a tradeoff
    - Typical socket call: sendto()
    - Thread class name: TelemetryBroadcastTask
    - Reads shared SystemState
    - Real-world analogy: Starlink Gateway Telemetry Channel
*/

#pragma once

#include "Task.hpp"
#include "SystemState.hpp"

#include <iostream>
#include <thread>
#include <chrono>
#include <string>
#include <sstream>
#include <mutex>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>


class TelemetryBroadcastTask : public Task {
public:
    TelemetryBroadcastTask(SystemState& sharedState,
                           const std::string& destIp = "127.0.0.1",
                           int destPort = 9100,
                           int intervalMs = 1000)
                           : Task("TelemetryBroadcastTask"),
                           state(sharedState),
                           destinationPort(destPort),
                           interval(intervalMs) {}
                           
protected:
    void run() override {
        int sock = socket(AF_INET, SOCK_DGRAM, 0);
        if (sock < 0) {
            std::cerr << "(Telemetry Broadcast) failed to create socket.\n";
            return;
        }

        sockaddr_in destAddr{};
        destAddr.sin_family = AF_INET;
        destAddr.sin_port = htons(destinationPort);
        destAddr.sin_addr.s_addr = inet_addr(destinationIp.c_str());

        while (running) {
            std::string telemetryMsg = serializeTelemetry();

            int sent = sendto(sock, telemetryMsg.c_str(), telemetryMsg.size(), 0,
                                (struct sockaddr*)&destAddr, sizeof(destAddr));

            if (sent < 0) {
                std::cerr << "(Telemetry Broadcast) Failed to send telemetry.\n";
            } else {
                std::cout << "(Telemetry Broadcast) Sent: " << telemetryMsg << "\n";
            }

            std::this_thread::sleep_for(std::chrono::milliseconds(interval));
        }
        
        close(sock);
    }

private:
    SystemState& state;
    std::string destinationIp;
    int destinationPort;
    int interval;

    std::string serializeTelemetry() {
        std::ostringstream oss;
        std::lock_guard<std::mutex> lock(state.mutex);

        oss <<"oxygen="<< state.oxygenLevel
            << ",battery=" << state.batteryLevel
            << ",fault=" << (state.faultRaised ? 1 : 0);

        return oss.str();
    }
};