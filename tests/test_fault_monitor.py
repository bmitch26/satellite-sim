# tests/test_fault_monitor.py

from cubesat.fault_monitor import FaultMonitorTask

def test_fault_monitor_detects_fault(capfd):
    from cubesat.fault_monitor import FaultMonitorTask

    task = FaultMonitorTask("FaultMonitor")
    state = {"tick": 5}
    task.run(state)

    out, _ = capfd.readouterr()
    assert "Overheating detected" in out  # <- this matches the output
