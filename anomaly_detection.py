import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    # Add any necessary preprocessing steps here
    return data

def detect_anomalies(data, features):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[features])
    
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(scaled_data)
    
    data['scores'] = model.decision_function(scaled_data)
    data['anomaly'] = model.predict(scaled_data)
    
    return data[data['anomaly'] == -1]

if __name__ == "__main__":
    file_path = 'path_to_network_traffic_data.csv'
    network_data = load_data(file_path)
    anomalies = detect_anomalies(network_data, ['src_bytes', 'dst_bytes'])
    
    print("Detected Anomalies:")
    print(anomalies)
