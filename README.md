# vitals-anomaly-simulator

## Description

This project simulates patient vitals and detects anomalies. It generates random vitals data for multiple patients, tags anomalies with patient IDs and timestamps, logs anomalies per patient, and publishes them to a Kafka topic.

## Getting Started

### Prerequisites

*   Python 3.9
*   Kafka

### Installation

1.  Clone the repository:

```bash
git clone <repository_url>
cd vitals-anomaly-simulator
```

2.  Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3.  Install the dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

1.  **Kafka Brokers**: Update the `KAFKA_BOOTSTRAP_SERVERS` in `src/main.py` with your Kafka broker addresses.
2.  **Number of Patients**: Modify the `NUM_PATIENTS` variable in `src/main.py` to simulate the desired number of concurrent patients.
3. **Kafka Topic**: Ensure that the topic `vitals_anomalies` is created in kafka.

### Usage

1.  Run the simulator:

```bash
python src/main.py
```

### Docker

1.  Build the Docker image:

```bash
docker build -t vitals-anomaly-simulator .
```

2.  Run the Docker container:

```bash
docker run -d vitals-anomaly-simulator
```

### Anomaly Logs

Anomalies are logged per patient in files named `anomaly_log_<patient_id>.txt`.

### Kafka Topic

Anomalies are published to the `vitals_anomalies` Kafka topic. Each message includes the `patient_id`, `timestamp`, `anomaly_type`, and `value`.
