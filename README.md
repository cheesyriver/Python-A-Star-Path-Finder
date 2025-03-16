# Python-A*-Path-Finder

This is a Python program that visualizes the A* pathfinding algorithm using Pygame.

## Features

* **Interactive Grid:** Users can create walls, set start and end nodes by clicking on the grid.
* **A* Algorithm Visualization:** The program visually demonstrates the A* algorithm's search process.
* **Path Reconstruction:** Once the path is found, it is highlighted on the grid.
* **Clear Grid:** Users can clear the grid and reset the start and end nodes.

## How to Run

1.  **Install Pygame:**
    ```bash
    pip install pygame
    ```

2.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `a_star_visualizer.py`).

3.  **Run the Program:**
    ```bash
    python a_star_visualizer.py
    ```

## Usage

* **Left Click:**
    * Click on an empty cell to set the start node (first click).
    * Click on another empty cell to set the end node (second click).
    * After setting the start and end nodes, click on empty cells to create walls.
* **Right Click:** Click on a cell to reset it (remove walls, start, or end node).
* **Spacebar:** Press the spacebar to start the A* algorithm.
* **'C' Key:** Press the 'C' key to clear the grid and reset the start and end nodes.
* **Close Window:** Close the window to exit the program.

## Code Explanation

* **Node Class:** Represents a cell in the grid, storing its position, color, and neighbors.
* **A* Algorithm:** Implemented using a priority queue to efficiently find the shortest path.
* **Heuristic Function (h):** Calculates the Manhattan distance between two nodes.
* **Grid Creation:** The `make_grid` function creates a 2D list of Node objects.
* **Drawing Functions:** Functions to draw the grid, nodes, and path.
* **Event Handling:** Handles mouse clicks and key presses to interact with the grid.

## Dependencies

* **Pygame:** Used for creating the graphical user interface.
* **Queue:** Used for the priority queue in the A* algorithm.
* **Math:** used for the absolute value function.

## Customization

* **Grid Size:** Modify the `ROWS` variable in the `main` function to change the grid size.
* **Window Size:** Modify the `WIN_WIDTH` variable to change the window size.
* **Colors:** Change the color constants (e.g., `RED`, `GREEN`, `BLACK`) to customize the appearance.

## Future Improvements

* Implement other pathfinding algorithms (e.g., Dijkstra's algorithm).
* Add options to change the grid size and algorithm speed.
* Create a more user-friendly interface with buttons and menus.