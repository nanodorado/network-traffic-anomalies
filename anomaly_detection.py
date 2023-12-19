import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from config import ANOMALY_THRESHOLD

def detect_anomalies(data, features):
    """
    Detect anomalies in data using the Isolation Forest algorithm.

    Parameters:
    data (DataFrame): The input data.
    features (list): List of feature column names.

    Returns:
    DataFrame: Data with anomaly scores and flags.
    """
    try:
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data[features])

        model = IsolationForest(n_estimators=100, contamination=ANOMALY_THRESHOLD, random_state=42)
        model.fit(scaled_data)

        data['scores'] = model.decision_function(scaled_data)
        data['anomaly'] = model.predict(scaled_data)
        
        return data
    except Exception as e:
        raise Exception(f"Error in anomaly detection: {e}")
