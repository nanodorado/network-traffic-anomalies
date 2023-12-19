# main.py
from data_loader import load_data
from anomaly_detection import detect_anomalies
from config import SUSPICIOUS_IPS

def check_suspicious_ips(data, ip_column):
    """
    Check for suspicious IPs in the data.

    Parameters:
    data (DataFrame): Data with anomalies.
    ip_column (str): Name of the IP address column.

    Returns:
    DataFrame: Data with suspicious IP flag.
    """
    data['suspicious_ip'] = data[ip_column].isin(SUSPICIOUS_IPS)
    return data[data['suspicious_ip']]

def temporal_analysis(data):
    """
    Perform temporal analysis on the data.

    Parameters:
    data (DataFrame): The input data.

    Returns:
    Series: Hourly counts of events.
    """
    data['hour'] = data['timestamp'].dt.hour
    return data.groupby('hour').count()['timestamp']

def send_notification(anomalies):
    """
    Send a notification for detected anomalies.

    Parameters:
    anomalies (DataFrame): Data containing detected anomalies.
    """
    if not anomalies.empty:
        print("Alerta de seguridad: Se han detectado anomalías")

if __name__ == "__main__":
    file_path = 'path_to_network_traffic_data.csv'
    network_data = load_data(file_path)
    anomalies = detect_anomalies(network_data, ['src_bytes', 'dst_bytes'])
    
    send_notification(anomalies)
    
    suspicious_activities = check_suspicious_ips(anomalies, 'src_ip')
    print("Actividades Sospechosas:")
    print(suspicious_activities)

    hourly_distribution = temporal_analysis(network_data)
    print("Distribución de tráfico por hora:")
    print(hourly_distribution)