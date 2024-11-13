import numpy as np
import time

def simulate_data_stream():
    """Simulates real-time data with seasonality and random anomalies."""
    t = 0
    while True:
        try:
            # Generate a sine wave with random noise
            data_point = 10 * np.sin(0.1 * t) + np.random.normal(0, 1)

            # Occasionally inject an anomaly with a 2% chance
            if np.random.rand() > 0.98:
                if np.random.rand() > 0.50:
                    data_point += np.random.normal(20, 5)
                else:
                    data_point += np.random.normal(-20, 5)

            yield data_point

            # Simulate real-time by sleeping for a short duration (0.1 seconds)
            time.sleep(0.1)
            t += 1        

        except Exception as e:
            print(f"\nError in data simulation: {e}") 
        