# Maze
Maze Generation and Solving in Python

![Screenshot](https://github.com/James-P-D/Maze/blob/master/screenshot.gif)

## Usage

After running the application a blank canvas will appear with a green and a red square at two opposing corners of the grid. The green cell will be the start position whilst the red cell will be the end position. The user can move either cell by dragging and dropping.

Once we have chosen suitable start and end cells, click the `CREATE MAZE` to generate the maze. The application uses the [Recursive Division algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_division_method). In addition is it possible toggle wall cells with the mouse pointer.

Once the maze has been fully generated, click the `SOLVE MAZE` button which will calculate the path between the start and end positions if such a path exists. The application uses the [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

## Setup

The program uses the following libraries:

[PyGame](https://www.pygame.org/) (I used v1.9.6 at the time but will probably work with latest version)

Hopefully [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)) should do the trick...

```
pip install pygame

```