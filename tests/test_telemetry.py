# tests/test_telemetry.py

from cubesat.telemetry import TelemetryTask

def test_telemetry_runs_without_error(capfd):
    buffer = []
    task = TelemetryTask("Telemetry", buffer)
    state = {"tick": 0}
    task.run(state)
    out, _ = capfd.readouterr()
    assert "TelemetryTask" in out
    assert buffer  # ensure packet was actually added
