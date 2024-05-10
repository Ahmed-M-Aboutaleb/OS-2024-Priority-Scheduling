class ProcessSchedule:
    def findHighestPriority(self, processes, time):
        highestPriorityProc = None
        highestPriority = float('Inf')
        for p in processes:
            if p.arrivalTime <= time and p.priority < highestPriority and p.burstTime > 0:
                highestPriority = p.priority
                highestPriorityProc = p
        return highestPriorityProc
    
    def priorityScheduling(self, processes):
        processes.sort(key=lambda x: x.arrivalTime)
        # Initialize time and completed processes count
        time = 0
        completed = 0
        n = len(processes)
        ganttChartData = {'Task': [], 'Start': [], 'Finish': []}
        totalWaitingTime = 0
        totalTurnaroundTime = 0
        totalResponseTime = 0
        while completed != n:
            # Find process with highest priority that has arrived
            highestPriorityProc = self.findHighestPriority(processes, time)

            if highestPriorityProc is None:
                # No process has arrived yet
                time += 1
            else:
                # Update time
                startTime = time
                time += highestPriorityProc.burstTime
                endTime = time
                # Add process execution to the Gantt chart data
                ganttChartData['Task'].append(f"Process {highestPriorityProc.pid}")
                ganttChartData['Start'].append(startTime)
                ganttChartData['Finish'].append(endTime)

                # Calculate waiting time and turnaround time
                waitingTime = startTime - highestPriorityProc.arrivalTime
                turnaroundTime = endTime - highestPriorityProc.arrivalTime
                responseTime = waitingTime  # For non-preemptive scheduling, waiting time is the same as response time

                highestPriorityProc.waitingTime = waitingTime
                highestPriorityProc.turnAroundTime = turnaroundTime

                totalWaitingTime += waitingTime
                totalTurnaroundTime += turnaroundTime
                totalResponseTime += responseTime

                # Mark process as completed
                highestPriorityProc.burstTime = 0
                completed += 1

        avgWaitingTime = totalWaitingTime / n
        avgTurnaroundTime = totalTurnaroundTime / n
        avgResponseTime = totalResponseTime / n

        return ganttChartData, avgWaitingTime, avgTurnaroundTime, avgResponseTime
