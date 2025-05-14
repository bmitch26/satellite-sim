# tests/test_fault_monitor.py

from cubesat.fault_monitor import FaultMonitorTask

def test_fault_monitor_detects_and_clears_fault(capfd):
    task = FaultMonitorTask("FaultMonitor")

    # Inject fault at tick 5
    state = {"tick": 5}
    task.run(state)
    out, _ = capfd.readouterr()
    assert "Fault injected" in out
    assert state["fault"] is True

    # Simulate reboot command
    state["tick"] = 6
    state["reboot_fault_monitor"] = True
    task.run(state)
    out, _ = capfd.readouterr()
    assert "Reboot command received" in out
    assert state["fault"] is False
