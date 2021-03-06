# Maze
Maze Generation and Solving in Python

![Screenshot](https://github.com/James-P-D/Maze/blob/master/screenshot.gif)

## Usage

After running the application a blank canvas will appear with a green and a red square at two opposing corners of the grid. The green cell will be the inital cell whilst the red cell will be the terminal cell. The user can move either cell by dragging and dropping:

![drag_drop](https://github.com/James-P-D/Maze/blob/master/drag_drop.gif)

Once we have chosen suitable start and end cells, click the `Create` to generate the maze. The application uses the [Recursive Division algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_division_method).

![create_maze](https://github.com/James-P-D/Maze/blob/master/create_maze.gif)

In addition is it possible toggle wall cells with the mouse pointer:

![toggle_cells](https://github.com/James-P-D/Maze/blob/master/toggle_cells.gif)

Once the maze has been fully generated, click the `DFS` or `BFS` buttons to calculate a path between the initial and terminal cell. In all cases cells that have been visited will appear in yellow whilst the final path will appear in blue.

### Depth First Search

The `DFS` button will perform a [depth first search](https://en.wikipedia.org/wiki/Depth-first_search) between initial and terminal cells. Note that the algorithm will terminate as soon as a valid path is found, rather than strictly finding the optimum path. Finally, depth first searching is the least efficient method of solving this type of problem and requires a lot of stack-space.

![dfs](https://github.com/James-P-D/Maze/blob/master/dfs.gif)

### Breadth First Search

The `BFS` button will perform a [breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search) between initial and terminal cells.

![bfs](https://github.com/James-P-D/Maze/blob/master/bfs.gif)

## Setup

The program uses the following libraries:

[pygame](https://www.pygame.org/) (Tested with v1.9.6)  
[numpy](https://numpy.org/) (Tested with v1.18.3)  

Hopefully [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)) should do the trick...

```
pip install pygame
pip install numpy

```