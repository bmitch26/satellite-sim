# tests/test_fault_monitor.py

from cubesat.fault_monitor import FaultMonitorTask

def test_fault_monitor_detects_fault(capfd):
    task = FaultMonitorTask("FaultMonitor")
    state = {"tick": 5}
    task.run(state)
    out, _ = capfd.readouterr()
    assert "Fault detected" in out
