import random
import time

class SHMSensor:
    """Class to simulate Structural Health Monitoring (SHM) sensors."""
    def __init__(self, sensor_type, threshold):
        self.sensor_type = sensor_type
        self.threshold = threshold

    def read_data(self):
        """Simulate sensor data reading."""
        return round(random.uniform(0, 100), 2)

    def analyze_data(self):
        """Check for abnormal values and trigger alerts."""
        data = self.read_data()
        print(f"{self.sensor_type} Sensor Reading: {data}")
        if data > self.threshold:
            print(f"⚠️ Alert! {self.sensor_type} exceeds threshold!")

def monitor_sensors(sensors, interval=5):
    """Continuously monitor a list of sensors at defined intervals."""
    try:
        while True:
            for sensor in sensors:
                sensor.analyze_data()
            print("-" * 30)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

# Define sensors
sensors = [
    SHMSensor("Vibration", 70),
    SHMSensor("Strain", 50)
]

# Start monitoring
monitor_sensors(sensors)