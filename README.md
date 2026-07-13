# Autonomous Warehouse Simulation with A* Pathfinding

A lightweight, terminal-based warehouse logistics simulator written in Python. The project uses the **A* (A-Star) search algorithm** to guide an otonomous mobile robot (AMR) through a dynamically generated grid layout with random obstacles, routing it efficiently to resolve industrial shelf barcodes.

---

## Features

* **A\* Pathfinding Algorithm:** Calculates the most mathematically optimal, obstacle-free route using Manhattan Distance as its heuristic function ($f(n) = g(n) + h(n)$).
* **Dynamic Grid Generation:** Generates customizable randomized maps with configurable obstacle density directly from a settings file.
* **Industrial Address Resolution:** Parses standard logistical shelf addresses (e.g., `A-04-02` representing Zone-Column-Row) into absolute $(X, Y)$ coordinate matrices.
* **Real-time Terminal Animation:** Clear-screen terminal rendering animates the robot's physical movement along the calculated path step-by-step.
* **Zero Dependencies:** Built entirely with standard native Python libraries (`time`, `random`). No external installations are required.

---

## Project Structure


warehouse-sim/
│
├── settings.py      # Simulation configurations (dimensions, probability, start)
├── address.py       # Logistical address parser (converts "A-XX-YY" to coordinate)
├── robot.py         # Node helper and Robot movement logic (A* implementation)
├── management.py    # Main orchestration script and terminal visualizer
└── README.md        # Project documentation

How to Run?

Ensure you have Python 3 installed on your machine. Clone or download the files into a single directory, open your terminal inside that directory, and run:
python management.py

Configuration
You can easily adjust the environment by editing the values in settings.py:
WIDTH = 9                  # Total grid columns (X-axis)
HEIGHT = 7                 # Total grid rows (Y-axis)
OBSTACLE_PROBABILITY = 0.25 # Percentage of grid populated by random shelves (0.0 to 1.0)
START_X = 0                # Robot's starting column
START_Y = 0                # Robot's starting row

Made by Ezgi Akbaş for my own portfolio.
