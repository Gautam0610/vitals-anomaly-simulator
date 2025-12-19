import os
import time
import json
from vitals_generator import generate_vitals

# Load environment variables
output_topic = os.environ.get("OUTPUT_TOPIC", "vitals_topic")
interval = int(os.environ.get("INTERVAL", 5))

while True:
    vitals = generate_vitals()
    print(f"Publishing to topic {output_topic}: {json.dumps(vitals)}")
    # Simulate publishing to a topic (replace with actual publishing logic)
    # publish_vitals(output_topic, vitals)
    time.sleep(interval)