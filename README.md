# Rubik's Cube Solver Using CPOF Algorithm 🧩

## Introduction 🌟

This project is designed to tackle the Rubik's Cube under the Fewest Moves Challenge (FMC) competition conditions but with a twist: solving must be completed within a mere 3 seconds! The solver averages an impressive 45 moves using the innovative Corners-First Optimal Pathfinding (CPOF) algorithm.

## Features 🚀

- **CPOF Algorithm**: Utilizes a corners-first strategy to efficiently solve the Rubik’s Cube. 🔄
- **Visualization**: Features a dynamic visualizer built with PyQt5, showcasing the cube's state throughout the solving process. 📊
- **Performance**: Leverages Numpy for high-performance mathematical computations to speed up the solving process. ⚡

## Installation 🔧

### Prerequisites

Ensure Python 3.x is installed on your system along with the PyQt5 and Numpy libraries. You can install these using pip:

```bash
pip install pyqt5 numpy vispy
```

## Getting Started 🚀

Clone this repository to your local machine to get started:

```bash
git clone https://github.com/Slpn/rubik
cd rubik
```

## Usage 📝

To run the solver, execute the script with a scramble as an argument. For example:

```bash
python3 src/main.py "F R U2 B' L' D'"
```

Generate a random scramble with a specified number of moves:

```bash
python3 src/main.py --generate 10
```

To visually trace the solving process:

```bash
python3 src/main.py --generate 10 --visualise
```

Evaluate the solver's performance:

```bash
python3 perfomance.py
```
