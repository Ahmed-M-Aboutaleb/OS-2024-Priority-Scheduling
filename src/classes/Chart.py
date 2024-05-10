import matplotlib.pyplot as plt
import pandas as pd

class Chart:
    def ganttChart(self, data):
        df = pd.DataFrame(data)
        fig, ax = plt.subplots()
        ax.barh(df['Task'], df['Finish'] - df['Start'], left=df['Start'], height=0.5, align='center')
        ax.set_xlabel('Time')
        ax.set_ylabel('Processes')
        ax.set_title('Priority (Non-Preemptive) Scheduling Gantt Chart')
        plt.grid(True)
        plt.show()