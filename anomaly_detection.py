import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import datetime

# Lista de IPs sospechosas para comparación (puede ser ampliada o integrada con una base de datos externa)
SUSPICIOUS_IPS = ['192.168.1.100', '10.0.0.2']

def load_data(file_path):
    data = pd.read_csv(file_path)
    # Conversión de la marca de tiempo a un formato de fecha/hora si es necesario
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    return data

def detect_anomalies(data, features):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[features])
    
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(scaled_data)
    
    data['scores'] = model.decision_function(scaled_data)
    data['anomaly'] = model.predict(scaled_data)
    
    return data

def check_suspicious_ips(data, ip_column):
    data['suspicious_ip'] = data[ip_column].isin(SUSPICIOUS_IPS)
    return data[data['suspicious_ip']]

def temporal_analysis(data):
    data['hour'] = data['timestamp'].dt.hour
    hourly_counts = data.groupby('hour').count()
    return hourly_counts['timestamp']

def send_notification(anomalies):
    # Esta función podría ser más compleja dependiendo del método de notificación
    print("Alerta de seguridad: Se han detectado anomalías")

if __name__ == "__main__":
    file_path = 'path_to_network_traffic_data.csv'
    network_data = load_data(file_path)
    anomalies = detect_anomalies(network_data, ['src_bytes', 'dst_bytes'])
    
    if not anomalies.empty:
        send_notification(anomalies)
    
    suspicious_activities = check_suspicious_ips(anomalies, 'src_ip')
    print("Actividades Sospechosas:")
    print(suspicious_activities)

    hourly_distribution = temporal_analysis(network_data)
    print("Distribución de tráfico por hora:")
    print(hourly_distribution)
