import matplotlib.pyplot as plt

class RealTimeVisualizer:
    def __init__(self):
        self.data = [] # Stores all data
        self.anomalies_data = [] # Stores only anomalous data

        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Data Points') # x axis shows the number of data points
        self.ax.set_ylabel('Data Value') # y axis shows the values of the data points

        self.line, = self.ax.plot([], [], lw=2) # Line to be drawn along data points
        self.anomalies, = self.ax.plot([], [], 'ro') # Anomalies are drawn with red dots

    def update(self, data_point, is_anomaly):
        try:
            # Validate the data point before adding
            if not isinstance(data_point, (int, float)):
                raise ValueError("Data point must be a number.")
            
            self.data.append(data_point) # Add the data point to the data list

            # Updates the line plot with the new data point
            self.line.set_xdata(range(len(self.data))) # x-value set to its position in the data list
            self.line.set_ydata(self.data) # y-value set to its value

            if is_anomaly:
                self.anomalies_data.append(data_point) # Add data point to the anomalous data lsit
            else:
                self.anomalies_data.append(None) # Add None to the anomalous data list to ensure the regular and anomalous data list stay aligned

            self.anomalies.set_xdata(range(len(self.anomalies_data)))
            self.anomalies.set_ydata(self.anomalies_data)

            # Adjust the axes to accomodate more data points
            self.ax.relim()
            self.ax.autoscale_view()

            plt.draw() # Re-draw the plot to show more points
            plt.pause(0.01) # Pause for 0.01 seconds to allow for GUI events
        except Exception as e:
            print(f"\nError in handling visualizer: {e}")