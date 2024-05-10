# CPU Priority Scheduling Simulator

This project is a simulation of the CPU Priority Scheduling algorithm for the Operating System 1 course.

## Table of Contents

-   [Introduction](#introduction)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Algorithm](#algorithm)
-   [Contributing](#contributing)
-   [License](#license)

## Introduction

The CPU Priority Scheduling Simulator is designed to simulate the behavior of the Priority Scheduling algorithm used in operating systems. It provides a visual representation of how processes with different priorities are scheduled and executed by the CPU.

## Installation

To install and run the simulator, follow these steps:

1. Clone the repository: `git clone https://github.com/Ahmed-M-Aboutaleb/OS1-2024-Priority-Scheduling.git`
2. Navigate to the project directory: `cd OS1-2024-Priority-Scheduling`
3. create a virtual environment: `python -m venv env`
4. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To start the simulator, run the following command:

```bash
python src
```

The simulator will open in a new window, allowing you to enter the number of processes and their priorities, brust time and arrival time. You can then start the simulation to see how the processes are scheduled and executed by the CPU.

## Algorithm

The Priority Scheduling algorithm is a non-preemptive scheduling algorithm that assigns priority to each process based on its importance. The process with the highest priority is selected for execution first. If two processes have the same priority, the process that arrived first is selected.

## Contributing

Contributions are welcome! Please feel free to submit a pull request if you have any improvements or new features to add to the simulator.

## License

This project is licensed under the [MIT License](LICENSE).
