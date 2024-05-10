class Process:
    def __init__(self, pid, arrivalTime, burstTime, priority):
        self.pid = pid
        self.setArrivalTime(arrivalTime)
        self.setBurstTime(burstTime)
        self.setPriority(priority)
        self.waitingTime = 0
        self.turnAroundTime = 0
    
    def setArrivalTime(self, arrivalTime):
        if arrivalTime < 0:
            raise ValueError('Arrival time must be greater than or equal to 0')
        self.arrivalTime = arrivalTime
        Process.arrivalTime = arrivalTime
    
    def setBurstTime(self, burstTime):
        if burstTime <= 0:
            raise ValueError('Brust time must be greater than 0')
        self.burstTime = burstTime
    
    def setPriority(self, priority):
        if priority < 0:
            raise ValueError('Priority must be greater than or equal to 0')
        self.priority = priority