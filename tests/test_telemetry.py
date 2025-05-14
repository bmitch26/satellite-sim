# tests/test_telemetry.py

from cubesat.telemetry import TelemetryTask

def test_telemetry_runs_without_error(capfd):
    task = TelemetryTask("Telemetry")
    state = {"tick": 0}
    task.run(state)
    out, _ = capfd.readouterr()
    assert "Sending telemetry" in out
