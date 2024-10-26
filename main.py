from data_stream import simulate_data_stream
from anomaly_detector import AnomalyDetector
from visualize import RealTimeVisualizer

# Initialize anomaly detector and the real time chart visualizer
detector = AnomalyDetector(window_size=50, threshold=3)
visualizer = RealTimeVisualizer()

def main():
    #Simulate a data stream
    for data_point in simulate_data_stream():
        # Pass each data point to the anomaly detector to check if it's an anomaly
        is_anomaly = detector.detect(data_point)

        # Visualize the data and any anomalies
        visualizer.update(data_point, is_anomaly)

if __name__ == "__main__":
    main()