import numpy as np
from collections import deque

class AnomalyDetector:
    def __init__(self, window_size=50, threshold=3):
        self.window_size = window_size # Anomalies are detected using a sliding window approach
        self.threshold = threshold # Data points with a z-score higher than the threshold will be flagged as anomalies
        self.window = deque(maxlen=window_size) # Holds only the 50 /window_size latest data points for efficient mean and standard deviation calculations

    def detect(self, data_point):
        try:
            # Check if data_point is a number
            if not isinstance(data_point, (int, float)):
                raise ValueError("Data point must be a number.")
            
            # Add point to the sliding window
            self.window.append(data_point)

            # If not enough data points to determine a mean and deviation, return False (no anomaly)
            if len(self.window) < self.window_size:
                return False
            
            # Calculate mean and standard deviation of the window
            mean = np.mean(self.window)
            std = np.std(self.window)

            # Z-score calculation
            z_score = (data_point - mean) / std if std != 0 else 0

            # Flag as anomaly if Z-score is above the threshold
            if abs(z_score) > self.threshold:
                print(f"\nAnomaly detected: {z_score}")
                return True
            
        except Exception as e:
            print(f"\nError in anomaly detection: {e}")
            
        return False
        
