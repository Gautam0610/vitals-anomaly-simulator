
import json
import random
import time
from datetime import datetime
import uuid
import threading
from kafka import KafkaProducer

# Configuration
KAFKA_TOPIC = "vitals_anomalies"
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']  # Replace with your Kafka brokers
NUM_PATIENTS = 50  # Number of concurrent simulated patients
VITALS_UPDATE_INTERVAL = 1  # in seconds

def generate_patient_id():
    return str(uuid.uuid4())

def generate_vitals(patient_id):
    heart_rate = random.randint(60, 100)
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    blood_pressure = f"{random.randint(110, 140)}/{random.randint(70, 90)}"
    respiratory_rate = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 99)

    # Introduce anomalies (example: heart rate)
    if random.random() < 0.05:  # 5% chance of anomaly
        heart_rate = random.randint(120, 150)  # High heart rate
        log_anomaly(patient_id, "High heart rate", heart_rate)

    return {
        "patient_id": patient_id,
        "timestamp": datetime.now().isoformat(),
        "heart_rate": heart_rate,
        "body_temperature": body_temperature,
        "blood_pressure": blood_pressure,
        "respiratory_rate": respiratory_rate,
        "oxygen_saturation": oxygen_saturation,
    }

def log_anomaly(patient_id, anomaly_type, value):
    timestamp = datetime.now().isoformat()
    log_message = f"Anomaly detected for patient {patient_id} at {timestamp}: {anomaly_type} - {value}"
    print(log_message)
    # You can extend this to log to a file or dedicated logging system
    with open(f"anomaly_log_{patient_id}.txt", "a") as log_file:
        log_file.write(log_message + "\n")
    publish_to_kafka(patient_id, timestamp, anomaly_type, value)

def publish_to_kafka(patient_id, timestamp, anomaly_type, value):
    try:
        producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        message = {
            "patient_id": patient_id,
            "timestamp": timestamp,
            "anomaly_type": anomaly_type,
            "value": value
        }
        producer.send(KAFKA_TOPIC, message)
        producer.flush()
        print(f"Published anomaly to Kafka for patient {patient_id}")
    except Exception as e:
        print(f"Error publishing to Kafka: {e}")

def simulate_patient_vitals(patient_id):
    while True:
        vitals = generate_vitals(patient_id)
        print(f"Vitals for patient {patient_id}: {vitals}")
        time.sleep(VITALS_UPDATE_INTERVAL)

def main():
    threads = []
    for _ in range(NUM_PATIENTS):
        patient_id = generate_patient_id()
        thread = threading.Thread(target=simulate_patient_vitals, args=(patient_id,))
        threads.append(thread)
        thread.start()

    # Keep the main thread alive
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
