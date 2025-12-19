# vitals-anomaly-simulator

This project simulates vitals data with occasional anomalies in heart rate and breaths per minute. It's designed for testing and demonstration purposes.

## Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/vitals-anomaly-simulator.git
    cd vitals-anomaly-simulator
    ```

2.  Build the Docker image:

    ```bash
    docker build -t vitals-anomaly-simulator .
    ```

3.  Run the Docker container:

    ```bash
    docker run -d -e OUTPUT_TOPIC=<your_output_topic> -e INTERVAL=<interval_in_seconds> vitals-anomaly-simulator
    ```

    Replace `<your_output_topic>` with the desired output topic and `<interval_in_seconds>` with the interval at which vitals data should be generated (in seconds).

## Configuration

The following environment variables can be configured:

*   `OUTPUT_TOPIC`: The topic to which vitals data will be published. Defaults to `vitals_topic`.
*   `INTERVAL`: The interval (in seconds) at which vitals data will be generated. Defaults to `5`.
