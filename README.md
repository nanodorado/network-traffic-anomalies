# Network Anomaly Detection

This Python script uses the Isolation Forest algorithm to detect anomalies in network traffic data, potentially indicative of security threats. It has been enhanced with temporal analysis, event correlation, and verification against a database of suspicious IP addresses.

## Features

- **Anomaly Detection**: Uses Isolation Forest to identify anomalous patterns in network traffic.
- **Temporal Analysis**: Analyzes traffic on an hourly basis to identify unusual patterns.
- **Event Correlation**: Compares events across different data sets to identify suspicious behaviors.
- **Suspicious IP List**: Compares detected IP addresses with a predefined list of IPs known for malicious activities.
- **Notifications**: Implements a basic notification system to alert about detected anomalies.

## Requirements

To run this script, you will need Python and some libraries. Install the dependencies with the following command:

```bash
pip install -r requirements.txt
