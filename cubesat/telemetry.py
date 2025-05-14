# cubesat/telemetry.py

from cubesat.utils import BaseTask
import json
import random
from datetime import datetime

class TelemetryTask(BaseTask):
    def __init__(self, name, buffer, interval=2):
        super().__init__(name, interval)
        self.buffer = buffer

    def run(self, state):
        self.last_run_tick = state["tick"]
        packet = TelemetryPacket(state["tick"])
        self.buffer.append(packet.to_dict())  # store raw dict
        state["last_telemetry_tick"] = state["tick"] 
        print(f"[TelemetryTask] Tick {state['tick']}: {packet.to_json()}")


class TelemetryPacket:
    def __init__(self, tick):
        self.packet_type = "TELEMETRY"
        self.packet_id = f"TM-{tick:04d}"
        self.destination = "GROUND"
        self.timestamp = datetime.utcnow().isoformat()
        self.tick = tick
        self.battery = round(random.uniform(70.0, 100.0), 2)
        self.temp = round(random.uniform(20.0, 40.0), 1)
        self.status = "OK" if self.battery > 85 else "WARN"

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)
    