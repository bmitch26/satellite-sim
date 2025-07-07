//// Task.hpp: ////

/*
This class sets the blueprint for all task threads. 

Purpose is to:
    - Provide a run() method to be implemented by each task.
    - Optionally stores the task name for logging or debugging.
    - Allows all tasks to be managed through std::unique_ptr<Task>.

Key design points:
    - start() method:               Launches task thread cleanly
    - join() method:                Ensures safe shutdown/cleanup
    - stop() with atomic<bool>      Allows safe, graceful shutdown across threads
    - virtual void run()            Forces each subclass to define its own logic
    - taskName field                Useful for logging/debugging/thread naming later
*/

#pragma once

#include <string>
#include <thread>
#include <atomic>

class Task {
private:
    std::thread taskThread;

protected:
    std::string taskName;
    std::atomic<bool> running;

    // main logic of the task; must be implemented in derived class
    virtual void run() = 0;

public:
    Task(const std::string& name) : taskName(name), running(true) {}

    // virtual destructor ensures proper cleanup in derived classes
    virtual ~Task() = default;

    // starts the task in a separate thread
    void start() {
        taskThread = std::thread(&Task::run, this);
    }

    // joins the thread (should be called during shutdown)
    void join() {
        if (taskThread.joinable()) {
            taskThread.join();
        }
    }

    // stops the task's main loop (thread-safe) 
    void stop() {
        running = false;
    }

    std::string getName() const {
        return taskName;
    }
};