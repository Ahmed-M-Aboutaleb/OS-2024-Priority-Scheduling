import tkinter as tk
from tkinter import messagebox
from classes import ProcessSchedule as PS
from classes import Process as P
from classes import Chart as C
from constants import Constants as Const

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry(Const.GEOMETRY)
        master.title(Const.TITLE)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.num_processes_label = tk.Label(self, text="Number of Processes")
        self.num_processes_label.grid(row=0, column=0)
        self.num_processes_entry = tk.Entry(self)
        self.num_processes_entry.grid(row=0, column=1)

        self.submit_button = tk.Button(self, text="SUBMIT", command=self.submit)
        self.submit_button.grid(row=1, column=0, columnspan=2)

    def submit(self):
        num_processes = self.num_processes_entry.get()

        if not num_processes.isdigit():
            messagebox.showerror("Invalid input", "Please enter a valid integer.")
            return

        num_processes = int(num_processes)

        self.num_processes_entry.delete(0, 'end')
        self.num_processes_label.grid_forget()
        self.num_processes_entry.grid_forget()
        self.submit_button.grid_forget()

        self.process_entries = []
        for i in range(num_processes):
            # Process ID is set automatically
            pid = i + 1

            arrival_time_label = tk.Label(self, text=f"Process {pid} Arrival Time")
            arrival_time_label.grid(row=i*3+2, column=0)
            arrival_time_entry = tk.Entry(self)
            arrival_time_entry.grid(row=i*3+2, column=1)

            burst_time_label = tk.Label(self, text=f"Process {pid} Burst Time")
            burst_time_label.grid(row=i*3+3, column=0)
            burst_time_entry = tk.Entry(self)
            burst_time_entry.grid(row=i*3+3, column=1)

            priority_label = tk.Label(self, text=f"Process {pid} Priority")
            priority_label.grid(row=i*3+4, column=0)
            priority_entry = tk.Entry(self)
            priority_entry.grid(row=i*3+4, column=1)

            self.process_entries.append((pid, arrival_time_entry, burst_time_entry, priority_entry))

        self.process_submit_button = tk.Button(self, text="SUBMIT PROCESSES", command=self.submit_processes)
        self.process_submit_button.grid(row=num_processes*3+2, column=0, columnspan=2)

    def submit_processes(self):
        processes = []
        for entries in self.process_entries:
            pid, arrival_time, burst_time, priority = (entry.get() if isinstance(entry, tk.Entry) else entry for entry in entries)

            if not (arrival_time.isdigit() and burst_time.isdigit() and priority.isdigit()):
                messagebox.showerror("Invalid input", "Please enter valid integers.")
                return

            processes.append(P.Process(int(pid), int(arrival_time), int(burst_time), int(priority)))

        processSchedule = PS.ProcessSchedule()
        chartData, avgWaitingTime, avgTurnaroundTime, avgResponseTime = processSchedule.priorityScheduling(processes)
        chart = C.Chart()
        chart.ganttChart(chartData)

        avgTimesLabel = tk.Label(self, text=f"Average Waiting Time: {avgWaitingTime}\nAverage Turnaround Time: {avgTurnaroundTime}\nAverage Response Time: {avgResponseTime}")
        avgTimesLabel.grid(row=len(self.process_entries)*3+3, column=0, columnspan=2)